import numpy as np
import PointUtils


def getPaths(self, entryPoints, targetPoints, ventricles):
    paths = {}
    for i in range(0, entryPoints.GetNumberOfMarkups()):
        entry = self.getCoordinates(entryPoints, i)
        for j in range(0, targetPoints.GetNumberOfMarkups()):
            target = self.getCoordinates(targetPoints, j)
            if not self.passThroughArea(entry, target, ventricles):
                key = tuple(entry)
                if key in paths:
                    paths[key].append(target)
                else:
                    paths[key] = target
    return paths

def passThroughArea(self, entry, target, area, subSampling, stepSize):
    xEntry, yEntry, zEntry = entry[0], entry[1], entry[2]
    xTarget, yTarget, zTarget = target[0], target[1], target[2]
    for t in np.arange(0, 1, stepSize):
        x, y, z = self.getXYZCoordinatesOnLine(xEntry, xTarget, yEntry, yTarget, zEntry, zTarget, t)
        pixelValue = PointUtils.getPixelValue(area, x, y, z, subSampling)
        if pixelValue == 1:
            return True
    return False

@staticmethod
def getCoordinateOnLine(entry, target, t):
    return entry + t * (target - entry)

def getXYZCoordinatesOnLine(self, xEntry, xTarget, yEntry, yTarget, zEntry, zTarget, t):
    x = self.getCoordinateOnLine(xEntry, xTarget, t)
    y = self.getCoordinateOnLine(yEntry, yTarget, t)
    z = self.getCoordinateOnLine(zEntry, zTarget, t)
    return x, y, z

# @staticmethod
# def passThroughVentricles(entry, target, ventricles):
#     xEntry, yEntry, zEntry = entry[0], entry[1], entry[2]
#     xTarget, yTarget, zTarget = target[0], target[1], target[2]
#     size = 10  # len(ventricles)
#     # line = Line3D(Point3D(xEntry, yEntry, zEntry), Point3D(xTarget, yTarget, zTarget))
#     for i in range(0, size):
#         [x, y, z] = ventricles[i]
#         # EvaluatePosition(): VTKLine
#         # if line.contains(Point3D(x, y, z)):
#         #     return True
#         xDivision = xTarget - xEntry
#         yDivision = yTarget - yEntry
#         zDivision = zTarget - zEntry
#         if xDivision != 0:
#             tx = (x - xEntry) / xDivision
#
#         if yDivision != 0:
#             ty = (y - yEntry) / yDivision
#
#         if zDivision != 0:
#             tz = (z - zEntry) / zDivision
#
#         if xDivision == 0:
#             if ty == tz:
#                 if ty > 0 or ty < 1:
#                     return True
#                 else:
#                     continue
#             else:
#                 continue
#
#         if yDivision == 0:
#             if tx == tz:
#                 if tx > 0 or tx < 1:
#                     return True
#                 else:
#                     continue
#             else:
#                 continue
#
#         if zDivision == 0:
#             if ty == tx:
#                 if ty > 0 or ty < 1:
#                     return True
#                 else:
#                     continue
#             else:
#                 continue
#
#         if tx == ty and ty == tz:
#             if tx > 0 or tx < 1:
#                 return True
#     return False