import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import pathing
from algorithmType import AlgorithmType


def generate_list_image(size):
    """

    :param size:
    :return: an 2D array encoded as list of list
    """
    return generate_numpy_image(size).tolist()


def generate_numpy_image(size):
    """

    :param size:
    :return: a 2D array encoded as a numpy array
    """
    image = np.random.rand(*size)
    return image


def display_image(originalImage, imageWithPath, algorithmType):
    """
    Display the original image and the image with path side by side
    :param originalImage: The original image with pixel densities
    :param imageWithPath: The image with the best path using the specified method
    :param algorithmType: The selected algorithm type
    """
    plt.subplot(1, 2, 1)
    plt.gca().set_title('Original')
    plt.imshow(originalImage)
    plt.subplot(1, 2, 2)
    plt.gca().set_title("Best Path: " + algorithmType.value)
    plt.imshow(imageWithPath)
    plt.show()


def display_image_with_best_path(originalImage, algorithmType, size=None):
    """
    Compute the best path and display it side by side with original
    :param originalImage: The original image with pixel densities
    :param size: The original image's size
    :param algorithmType: The selected algorithm type
    """
    imageWithPath = pathing.getAdjustedImageArray(originalImage, algorithmType, size)
    display_image(originalImage, imageWithPath, algorithmType)


def get_image_with_best_path(originalImage, algorithmType, size=None):
    """
    Get an image that contains the best path
    :param originalImage: The original image with pixel densities
    :param size: The original image's size
    :param algorithmType: The selected algorithm type
    :returns: an image with the best path
    """
    return pathing.getAdjustedImageArray(originalImage, algorithmType, size)


def compare_both_methods(originalImage, size=None):
    """
    This methods puts the paths of the two solutions next to each other so that we can make sure they both find the same
    best path
    :param originalImage: The original image with pixel densities
    :param size: The original image's size
    """
    imageWithPathNaive = pathing.getAdjustedImageArray(originalImage, AlgorithmType.BRUTE_FORCE, size)
    imageWithPathDynamic = pathing.getAdjustedImageArray(originalImage, AlgorithmType.DYNAMIC, size)
    display_images_for_comparison(originalImage, imageWithPathNaive, imageWithPathDynamic)


def display_images_for_comparison(originalImage, imageWithPathNaive, imageWithPathDynamic):
    """
    This methods puts the paths of the two solutions next to each other so that we can make sure they both find the same
    best path
    :param originalImage: The original image with pixel densities
    :param imageWithPathNaive: The image with the best path using the naive method
    :param imageWithPathDynamic: The image with the best path using the dynamic method
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Comparing the two methods')
    ax1.imshow(originalImage)
    ax2.imshow(imageWithPathNaive)
    ax3.imshow(originalImage)
    ax4.imshow(imageWithPathDynamic)
    plt.show()
