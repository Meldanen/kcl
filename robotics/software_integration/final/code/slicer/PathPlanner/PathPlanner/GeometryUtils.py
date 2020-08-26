import vtk
import numpy as np


def isValidAngle(tree, polyData, entryPoint, targetPoint, specifiedAngle):
    entry = [entryPoint[0], entryPoint[1], entryPoint[2]]
    target = [targetPoint[0], targetPoint[1], targetPoint[2]]
    trianglePoints = vtk.vtkPoints()
    trianglePointIds = vtk.vtkIdList()
    trianglePointsCell = vtk.vtkIdList()

    tree.IntersectWithLine(entry, target, trianglePoints, trianglePointIds)
    intersectionPoint = trianglePoints.GetPoint(0)
    polyData.GetCellPoints(trianglePointIds.GetId(0), trianglePointsCell)

    point1, point2, point3 = getTrianglePoints(trianglePointsCell, polyData)
    angle = getAngle(entryPoint, intersectionPoint, point1, point2, point3)
    return angle < specifiedAngle


def getAngle(entryPoint, intersectionPoint, point1, point2, point3):
    trianglePerpendicularVector = getTrianglePerpendicularVector(point1, point2, point3)
    vectorFromPoints = getVectorFromPoints(intersectionPoint, entryPoint)
    return getAngleOfTwoVectors(trianglePerpendicularVector, vectorFromPoints)


def getTrianglePoints(pointsInCell, polyData):
    point1 = polyData.GetPoint(pointsInCell.GetId(0))
    point2 = polyData.GetPoint(pointsInCell.GetId(1))
    point3 = polyData.GetPoint(pointsInCell.GetId(2))
    return point1, point2, point3


def getAngleOfTwoVectors(vector1, vector2):
    vectorProduct = np.dot(vector1, vector2)
    vectorMagnitude1 = getVectorMagnitude(vector1)
    vectorMagnitude2 = getVectorMagnitude(vector2)
    return np.degrees(vectorProduct / (vectorMagnitude1 * vectorMagnitude2))


def getVectorMagnitude(vector):
    return np.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)


def getTrianglePerpendicularVector(point1, point2, point3):
    vector1 = getVectorFromPoints(point1, point2)
    vector2 = getVectorFromPoints(point1, point3)
    return np.cross(vector1, vector2)


def getVectorFromPoints(point1, point2):
    return [point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2]]
