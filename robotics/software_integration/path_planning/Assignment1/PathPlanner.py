import vtk
import GeometryUtils
import PointUtils
import numpy as np
import sitkUtils as su
import SimpleITK as sitk


# Hard Constraints
def applyAllHardConstraints(entries, targets, hippocampus, ventricles, vessels, cortex, specifiedAngle):
    trajectoryDictionary = {}
    # Filter targets
    entriesAndTargets = preProcessing(entries, hippocampus, targets)

    # Create the OBB tree for each area
    ventriclesTree, _ = getTree(ventricles)
    bloodVesselTree, _ = getTree(vessels)
    cortexTree, cortexPolyData = getTree(cortex, (0, 0.5))
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            # First check if it passes through a ventricle - fastest check
            if isPassThroughArea(ventriclesTree, entry, target):
                continue
            # Then check if it passes through a blood vessel - medium speed check
            if isPassThroughArea(bloodVesselTree, entry, target):
                continue
            # finally check for the specified angle - slow check
            if not isValidAngle(cortexTree, cortexPolyData, entry, target, specifiedAngle):
                continue
            # Add to dictionary of accepted paths
            key = tuple(entry)
            if key in trajectoryDictionary:
                trajectoryDictionary[key].append(target)
            else:
                trajectoryDictionary[key] = [target]
    return trajectoryDictionary


def preProcessing(entries, hippocampus, targets):
    filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
    return PointUtils.convertEntryAndTargetPointsToDictionary(entries, filteredTargets)


# Checks if the trajectory passes through an undesired area
def getTrajectoriesAvoidingArea(entriesAndTargets, area):
    trajectoryDictionary = {}
    tree, _ = getTree(area)
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            if not isPassThroughArea(tree, entry, target):
                key = tuple(entry)
                if key in trajectoryDictionary:
                    trajectoryDictionary[key].append(target)
                else:
                    trajectoryDictionary[key] = [target]
    return trajectoryDictionary


def getTree(area, value=None):
    polyData = getMesh(area, value).GetOutput()
    tree = vtk.vtkOBBTree()
    tree.SetDataSet(polyData)
    tree.BuildLocator()
    return tree, polyData


def getMesh(area, value):
    if value is not None:
        mesh = getStandardMesh(area, value)
    else:
        mesh = getDiscreteMesh(area)
    mesh.Update()
    return mesh


def getDiscreteMesh(area):
    mesh = vtk.vtkDiscreteMarchingCubes()
    mesh.SetInputData(area.GetImageData())
    return mesh


def getStandardMesh(area, value):
    mesh = vtk.vtkMarchingCubes()
    mesh.SetInputData(area.GetImageData())
    mesh.SetValue(value[0], value[1])
    return mesh


def isPassThroughArea(tree, entry, target):
    trianglePoints = vtk.vtkPoints()
    trianglePointsId = vtk.vtkIdList()
    return tree.IntersectWithLine(entry, target, trianglePoints, trianglePointsId) != 0


# Checks if the trajectory passes enters at an undesired angle
def getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, specifiedAngle):
    trajectoryDictionary = {}
    tree, polyData = getTree(cortex, (0, 0.5))
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            if GeometryUtils.isValidAngle(tree, polyData, entry, target, specifiedAngle):
                key = tuple(entry)
                if key in trajectoryDictionary:
                    trajectoryDictionary[key].append(target)
                else:
                    trajectoryDictionary[key] = [target]
    return trajectoryDictionary


def isValidAngle(tree, polyData, entry, target, specifiedAngle):
    return GeometryUtils.isValidAngle(tree, polyData, entry, target, specifiedAngle)


# Soft Constraint
def getBestTrajectory(entriesAndTargets, area, precision):
    tree, _ = getTree(area)
    sortedPointsAccordingToDistance = getSortedPathsAccordingToDistance(entriesAndTargets, tree, precision)
    mostDistance = sortedPointsAccordingToDistance[0]
    leastDistance = sortedPointsAccordingToDistance[-1]
    return mostDistance, leastDistance


def getSortedPathsAccordingToDistance(entriesAndTargets, tree, precision):
    sortedPointsAccordingToDistance = {}
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            distance = 0
            distance += getDistanceOfClosestPointToPath(entry, target, tree, precision)
            key = float(distance)
            if key in sortedPointsAccordingToDistance.keys():
                sortedPointsAccordingToDistance[key].append([entry, target])
            else:
                sortedPointsAccordingToDistance[key] = [entry, target]
    sortedPointsAccordingToDistance = sorted(sortedPointsAccordingToDistance.items(), reverse=True)
    return sortedPointsAccordingToDistance


def getDistanceOfClosestPointToPath(entry, target, tree, precision):
    minDistance = 0
    xEntry, yEntry, zEntry = entry[0], entry[1], entry[2]
    xTarget, yTarget, zTarget = target[0], target[1], target[2]
    for step in np.arange(0, 1, precision):
        x, y, z = PointUtils.getXYZPointsOnLine(step, xEntry, xTarget, yEntry, yTarget, zEntry, zTarget)
        distance = getClosestPointDistance(tree, x, y, z)
        vector = GeometryUtils.getVectorFromPoints(entry, target)
        minDistance = GeometryUtils.getVectorMagnitude(vector)
        if distance > 0 and distance < minDistance:
            minDistance = distance
    return minDistance


def getClosestPointDistance(tree, x, y, z):
    closestPoint = [0.0, 0.0, 0.0]
    cellId = vtk.reference(0)
    subId = vtk.reference(0)
    distance = vtk.reference(0)
    tree.FindClosestPoint((x, y, z), closestPoint, cellId, subId, distance)
    return distance
