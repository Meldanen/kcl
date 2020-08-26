from itertools import chain
import math
from algorithmType import AlgorithmType
import numpy as np


def getAdjustedImageArray(image, algorithmType, size=None):
    """
    Returns an image with the best path based on the selected method
    :param image: The image from which we'll look for the best path
    :param size: The image's size
    :param algorithmType: The algorithm type (i.e. dynamic)
    :return: an image that includes the best path
    """
    validateAlgorithmType(algorithmType)
    validateImage(image)
    return getImageWithBestPath(image, size, algorithmType)


def getImageWithBestPath(image, size, algorithmType):
    """
    Returns an image with the best path based on the selected method
    :param image: The image from which we'll look for the best path
    :param size: The image's size
    :param algorithmType: The algorithm type (i.e. dynamic)
    :return: an image that includes the best path
    :raises: NotImplementedError if the algorithm type is not one of the implemented ones
    """
    if algorithmType is algorithmType.BRUTE_FORCE:
        return getImageWithBestPathBruteForce(image, size)
    elif algorithmType is algorithmType.DYNAMIC:
        return getImageWithBestPathDynamic(image)
    raise NotImplementedError


def getImageWithBestPathDynamic(image):
    """
    Returns an image with the best path
    :param image: The image from which we'll look for the best path
    :return: an image with the best path
    """
    if not isinstance(image, np.ndarray):
        image = np.array(image)
    costArray, backtrack = getCostAndBacktrackArrays(image)
    rows, columns = image.shape
    imageWithBestPath = np.zeros((rows, columns), dtype=np.int)
    j = np.argmin(costArray[-1])
    for i in reversed(range(rows)):
        imageWithBestPath[i, j] = 1
        j = backtrack[i, j]
    return imageWithBestPath


def getCostAndBacktrackArrays(image):
    """
    Computes the cost array which contains the best path and a backtrack array to trace the steps
    :param image: The image from which we'll look for the best path
    :return: a cost array for the best path and the backtrack array
    """
    rows, columns = image.shape
    cost = image.copy()
    backtrack = np.zeros_like(cost, dtype=np.int)
    cost[0, :] = 0
    for i in range(1, rows):
        for j in range(0, columns):
            # Make sure we don't try to use a negative index if we're on the left edge
            if j == 0:
                previousCosts = cost[i - 1, j:j + 2]
                costOfCurrentPaths = abs(image[i - 1, j:j + 2] - image[i, j])
                indexOfBestNode = np.argmin(previousCosts + costOfCurrentPaths)
                backtrack[i, j] = indexOfBestNode + j
                costBetweenTheTwoNodes = abs(image[i - 1, indexOfBestNode + j] - image[i, j])
                previousCost = cost[i - 1, indexOfBestNode + j]
                cost[i, j] = previousCost + costBetweenTheTwoNodes
            else:
                previousCosts = cost[i - 1, j - 1:j + 2]
                costOfCurrentPaths = abs(image[i - 1, j - 1:j + 2] - image[i, j])
                indexOfBestNode = np.argmin(previousCosts + costOfCurrentPaths)
                backtrack[i, j] = indexOfBestNode + j - 1
                costBetweenTheTwoNodes = abs(image[i - 1, indexOfBestNode + j - 1] - image[i, j])
                previousCost = cost[i - 1, indexOfBestNode + j - 1]
                cost[i, j] = previousCost + costBetweenTheTwoNodes
    return cost, backtrack


def getImageWithBestPathBruteForce(image, size):
    """
    Creates all the possible paths and then finds the best one
    :param image: The image from which we'll look for the best path
    :param size: The image's size
    :return: an image with the best path
    """
    size = getSize(image, size)
    validateSize(size)
    rows, columns = size
    paths = None
    for i in range(columns):
        if paths is None:
            paths = getAllPossiblePathsBruteForce(image, 0, i, rows - 1)
        else:
            paths = chain(paths, getAllPossiblePathsBruteForce(image, 0, i, rows - 1))
    bestPath = getBestPathBruteForce(image, paths)
    return convertBestPathToImageWithBestPathBruteForce(image, bestPath, rows, columns)


def convertBestPathToImageWithBestPathBruteForce(image, bestPath, rows, columns):
    """
    Converts the best path to an image with the best path
    Not entirely sure if we need to return a different type depending on the initial one but I included it just in case
    :param image: The image from which we'll look for the best path
    :param bestPath: The best path
    :param rows: The image's rows
    :param columns: The image's columns
    :return: an image with the best path
    """
    if isinstance(image, np.ndarray):
        return getImageWithBestPathForNumpyArray(bestPath, rows, columns)
    return getImageWithBestPathForPythonList(bestPath, rows, columns)


def getImageWithBestPathForPythonList(bestPath, rows, columns):
    """
    Converts the best path to an python list with the best path
    :param bestPath: The best path
    :param rows: The image's rows
    :param columns: The image's columns
    :return: an image with the best path
    """
    imageWithBestPath = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if (i, j) in bestPath:
                imageWithBestPath[i][j] = 1
    return imageWithBestPath


def getImageWithBestPathForNumpyArray(bestPath, rows, columns):
    """
    Converts the best path to a numpy array with the best path
    :param bestPath: The best path
    :param rows: The image's rows
    :param columns: The image's columns
    :return: an image with the best path
    """
    imageWithBestPath = np.zeros((rows, columns), dtype=np.int)
    for i in range(rows):
        for j in range(columns):
            if (i, j) in bestPath:
                imageWithBestPath[i, j] = 1
    return imageWithBestPath


def getBestPathBruteForce(image, paths):
    """
    Evaluates all paths in the image to find the best one
    :param image: The image from which we'll look for the best path
    :param paths: All the possible paths
    :return: The best path
    """
    bestScore = math.inf
    bestPath = None
    for path in paths:
        score = 0
        for i, j in path:
            # Stop if we reached the last node
            if i + 1 < len(path):
                x = path[i][0]
                y = path[i][1]
                w = path[i + 1][0]
                z = path[i + 1][1]
                value1 = image[x][y]
                value2 = image[w][z]
                score += abs(value1 - value2)
        if score < bestScore:
            bestScore = score
            bestPath = path
    return bestPath


def getAllPossiblePathsBruteForce(image, i, j, rows, current_path=None):
    """
    Calculates all the possible paths in the image
    :param image: The image from which we'll look for the best path
    :param i: The current row
    :param j: The current column
    :param rows: The total rows
    :param current_path: The current path
    :return: a list with all possible paths
    """
    if current_path is None:
        current_path = [(i, j)]
    if i == rows:
        yield current_path
    else:
        for x, y in getPossibleNeighbors(image, i, j):
            if (x, y) not in current_path:
                for path in getAllPossiblePathsBruteForce(image, x, y, rows, current_path + [(x, y)]):
                    yield path


def getPossibleNeighbors(image, i, j):
    """
    Finds the possible neighbours from the current point
    :param image: The image from which we'll look for the best path
    :param i: The current row
    :param j: The current column
    :return:
    """
    for x, y in getAdjacentCells(i, j):
        if 0 <= x < len(image[0]) and 0 <= y < len(image):
            yield (x, y)


def getAdjacentCells(i, j):
    """
    Returns the direction of movement from the current node
    :param i: The current row
    :param j: The current column
    :return: The direction of movement from the current node
    """
    yield (i + 1, j - 1)
    yield (i + 1, j)
    yield (i + 1, j + 1)


def validateAlgorithmType(algorithmType):
    """
    :param algorithmType: The solution method (i.e. dynamic)
    :raises ValueError: if the algorithm type is invalid
    """
    if algorithmType is None or not isinstance(algorithmType, AlgorithmType):
        raise TypeError("Please use a valid algorithm type")


def validateImage(image):
    """
    :param image: The image from which we'll look for the best path
    :raises ValueError: if the image is invalid
    """
    if image is None or len(image) == 0:
        raise ValueError("Image is empty or null")


def validateSize(size):
    """
    :param size: The image's size
    :raises ValueError: if the size is invalid
    """
    if size is None or size[0] <= 0 or size[1] <= 0:
        raise ValueError("Dimensions must be greater than zero")


def getSize(image, size):
    """
    Get the size of the image
    :param image: The image from which we'll look for the best path
    :param size: If it's provided, we assume the user knows what they are doing
    :return: the size of the image
    """
    if size is not None:
        return size
    if isinstance(image, np.ndarray):
        return getNumpyArraySize(image)
    return getPythonListSize(image)


def getNumpyArraySize(image):
    """
    Get the size of the image for numpy arrays
    :param image: The image from which we'll look for the best path
    :return: the size of the image
    """
    return image.shape


def getPythonListSize(image):
    """
    The size of the image for python lists.
    If the length of a sublist is inconsistent (i.e. [[1,2,3], [1,2], [1,2,3]]) we raise an exception
    :param image: The image from which we'll look for the best path
    :return: the size of the image
    :raises ValueError: For inconsistent image dimensions
    """
    rows = len(image)
    columns = None
    for column in image:
        if columns is None:
            columns = len(column)
        if len(column) != columns or columns != rows:
            raise ValueError("Image dimensions are inconsistent")
    return rows, columns
