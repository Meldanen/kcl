import vtk


def getCoordinates(points, pointIndex):
    pos = [0, 0, 0]
    points.GetNthFiducialPosition(pointIndex, pos)
    return pos


def getPixelValue(area, target, xMax, yMax, zMax):
    xIndex, yIndex, zIndex = getXYZCoordinateFromVoxelId(area, target, xMax, yMax, zMax)
    return area.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0)


def getXYZCoordinateFromVoxelId(area, target, xMax, yMax, zMax):
    imageVoxelID = area.GetImageData().FindPoint(target[0], target[1], target[2])
    xIndex = int(imageVoxelID % xMax)
    yIndex = int((imageVoxelID / xMax) % yMax)
    zIndex = int((imageVoxelID / (xMax * yMax)) % zMax)
    return xIndex, yIndex, zIndex


def getFilteredTargets(targetsNode, area):
    filteredTargets = []
    [xMax, yMax, zMax] = area.GetImageData().GetDimensions()
    for i in range(0, targetsNode.GetNumberOfMarkups()):
        target = getCoordinates(targetsNode, i)
        if getPixelValue(area, target, xMax, yMax, zMax) != 0:
            filteredTargets.append(target)
    return filteredTargets


# Provided code
def printEntryAndTargetsInDict(entriesAndTargets):
    # we are going to create a poly data defined by a set of points and lines
    points = vtk.vtkPoints()  # these are our end/start points
    lines = vtk.vtkCellArray()  # these are the lines connecting them
    for entry, targets in entriesAndTargets.items():
        entryId = points.InsertNextPoint(entry[0], entry[1], entry[2])
        for target in targets:
            targetInd = points.InsertNextPoint(target[0], target[1], target[2])

            # how to connect my points
            line = vtk.vtkLine()
            line.GetPointIds().SetId(0, entryId)
            line.GetPointIds().SetId(1, targetInd)
            lines.InsertNextCell(line)

    myPaths = vtk.vtkPolyData()
    myPaths.SetPoints(points)
    myPaths.SetLines(lines)
    return myPaths


def getEntriesAndTargetsInDict(entries, targets):
    paths = {}
    for i in range(0, entries.GetNumberOfMarkups()):
        entry = getCoordinates(entries, i)
        for target in targets:
            key = tuple(entry)
            if key in paths:
                paths[key].append(target)
            else:
                paths[key] = [target]

    return paths


def convertMarkupNodeToPoints(markupNode):
    newTargets = []
    for i in range(0, markupNode.GetNumberOfMarkups()):
        target = getCoordinates(markupNode, i)
        newTargets.append(target)
    return newTargets
