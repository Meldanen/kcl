import vtk


def getPoints(inputVolume, inputFiducials, outputFiducials):
    outputFiducials.RemoveAllMarkups()
    # we can get a transformation from our input volume
    mat = vtk.vtkMatrix4x4()
    inputVolume.GetRASToIJKMatrix(mat)

    # set it to a transform type
    transform = vtk.vtkTransform()
    transform.SetMatrix(mat)

    for x in range(0, inputFiducials.GetNumberOfFiducials()):
        pos = getCoordinates(inputFiducials, x)
        # get index from position using our transformation
        ind = transform.TransformPoint(pos)

        # get pixel using that index
        pixelValue = getPixelValueFromIndices(inputVolume, int(ind[0]), int(ind[1]), int(ind[2]))
        if pixelValue == 1:
            outputFiducials.AddFiducial(pos[0], pos[1], pos[2])
    return outputFiducials


def getPixelValue(area, x, y, z, subSampling):
    xIndex, yIndex, zIndex = getXYZIndices(area, x, y, z, subSampling)
    return getPixelValueFromIndices(area, xIndex, yIndex, zIndex)


def getPixelValueFromIndices(area, xIndex, yIndex, zIndex):
    return area.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0)


def getXYZIndices(area, x, y, z, subSampling):
    imageVoxelID = area.GetImageData().FindPoint(x / subSampling, y / subSampling, z / subSampling)
    xIndex = int(imageVoxelID % x)
    yIndex = int(imageVoxelID % (x * y) / x)
    zIndex = int((imageVoxelID / (x * y)))
    return xIndex, yIndex, zIndex


def getCoordinates(inputFiducials, x):
    pos = [0, 0, 0]
    inputFiducials.GetNthFiducialPosition(x, pos)
    return pos
