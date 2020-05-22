import vtk


# Filter for targets that are within the specified area
def getFilteredTargets(targets, area):
    filteredTargets = []
    mat = vtk.vtkMatrix4x4()
    area.GetRASToIJKMatrix(mat)

    # set it to a transform type
    transform = vtk.vtkTransform()
    transform.SetMatrix(mat)

    for x in range(0, targets.GetNumberOfFiducials()):
        pos = [0, 0, 0]
        targets.GetNthFiducialPosition(x, pos)
        # get index from position using our transformation
        index = transform.TransformPoint(pos)
        xIndex, yIndex, zIndex = int(index[0]), int(index[1]), int(index[2])

        # get pixel using that index
        pixelValue = area.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0)
        if pixelValue != 0:
            filteredTargets.append(index)
    return filteredTargets


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


# Provided code
def convertEntryTargetDictionaryToVtkObject(entriesAndTargets):
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

    trajectories = vtk.vtkPolyData()
    trajectories.SetPoints(points)
    trajectories.SetLines(lines)
    return trajectories

# Provided code
def convertEntryTargetPairToVtkObject(entryAndTarget):
    # we are going to create a poly data defined by a set of points and lines
    points = vtk.vtkPoints()  # these are our end/start points
    lines = vtk.vtkCellArray()  # these are the lines connecting them

    entry = entryAndTarget[0]
    target = entryAndTarget[1]
    entryId = points.InsertNextPoint(entry[0], entry[1], entry[2])
    targetInd = points.InsertNextPoint(target[0], target[1], target[2])

    # how to connect my points
    line = vtk.vtkLine()
    line.GetPointIds().SetId(0, entryId)
    line.GetPointIds().SetId(1, targetInd)
    lines.InsertNextCell(line)

    trajectories = vtk.vtkPolyData()
    trajectories.SetPoints(points)
    trajectories.SetLines(lines)
    return trajectories


def convertEntryAndTargetPointsToDictionary(entries, targets):
    trajectories = {}
    for i in range(0, entries.GetNumberOfMarkups()):
        entry = getCoordinates(entries, i)
        for target in targets:
            key = tuple(entry)
            if key in trajectories:
                trajectories[key].append(target)
            else:
                trajectories[key] = [target]
    return trajectories


def convertMarkupNodeToPoints(markupNode):
    newTargets = []
    for i in range(0, markupNode.GetNumberOfMarkups()):
        target = getCoordinates(markupNode, i)
        newTargets.append(target)
    return newTargets


def getXYZPointsOnLine(step, xEntry, xTarget, yEntry, yTarget, zEntry, zTarget):
    x = getPointsOnLine(xTarget, xEntry, step)
    y = getPointsOnLine(yTarget, yEntry, step)
    z = getPointsOnLine(zTarget, zEntry, step)
    return x, y, z


def getPointsOnLine(step, entry, target):
    return entry + step * (target - entry)
