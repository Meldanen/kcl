import vtk
import GeometryUtils


def applyAllConstraints(entriesAndTargets, ventricles, vessels, cortex, specifiedAngle):
    entryTargetDictionary = {}
    ventriclesTree, _ = getTree(ventricles)
    bloodVesselTree, _ = getTree(vessels)
    cortexTree, cortexPolyData = getTree(cortex, (0, 0.5))
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            if isPassThroughArea(ventriclesTree, entry, target):
                continue
            if isPassThroughArea(bloodVesselTree, entry, target):
                continue
            if not isValidAngle(cortexTree, cortexPolyData, entry, target, specifiedAngle):
                continue
            key = tuple(entry)
            if key in entryTargetDictionary:
                entryTargetDictionary[key].append(target)
            else:
                entryTargetDictionary[key] = [target]
    return entryTargetDictionary


def getEntryTargetDictionaryAvoidingArea(entriesAndTargets, area):
    entryTargetDictionary = {}
    tree, _ = getTree(area)
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            if not isPassThroughArea(tree, entry, target):
                key = tuple(entry)
                if key in entryTargetDictionary:
                    entryTargetDictionary[key].append(target)
                else:
                    entryTargetDictionary[key] = [target]
    return entryTargetDictionary


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


def getEntryTargetDictionaryWithSpecifiedAngle(entriesAndTargets, cortex, specifiedAngle):
    entryTargetDictionary = {}
    tree, polyData = getTree(cortex, (0, 0.5))
    for entry, targets in entriesAndTargets.items():
        for target in targets:
            if GeometryUtils.isValidAngle(tree, polyData, entry, target, specifiedAngle):
                key = tuple(entry)
                if key in entryTargetDictionary:
                    entryTargetDictionary[key].append(target)
                else:
                    entryTargetDictionary[key] = [target]
    return entryTargetDictionary


def isValidAngle(tree, polyData, entry, target, specifiedAngle):
    return GeometryUtils.isValidAngle(tree, polyData, entry, target, specifiedAngle)
