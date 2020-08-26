import generate_images
from algorithmType import AlgorithmType
import time

if __name__ == "__main__":
    size = (10, 10)
    # Generate some images
    # list_image = generate_images.generate_list_image(size)

    # Some example of how the code can be used
    # With NumPy
    np_image = generate_images.generate_numpy_image(size)
    start = time.time()
    generate_images.get_image_with_best_path(np_image, AlgorithmType.BRUTE_FORCE)
    end = time.time()
    print("Total time for - ", AlgorithmType.BRUTE_FORCE.value, ": ", end - start)

    start = time.time()
    generate_images.get_image_with_best_path(np_image, AlgorithmType.DYNAMIC)
    end = time.time()
    print("Total time for - ", AlgorithmType.DYNAMIC.value, ": ", end - start)

    generate_images.display_image_with_best_path(np_image, AlgorithmType.BRUTE_FORCE)
    generate_images.display_image_with_best_path(np_image, AlgorithmType.DYNAMIC)
    generate_images.compare_both_methods(np_image)

    # With a python list
    list_image = np_image.tolist()
    start = time.time()
    generate_images.get_image_with_best_path(list_image, AlgorithmType.BRUTE_FORCE)
    end = time.time()
    print("Total time for - ", AlgorithmType.BRUTE_FORCE.value, ": ", end - start)

    start = time.time()
    generate_images.get_image_with_best_path(list_image, AlgorithmType.DYNAMIC)
    end = time.time()
    print("Total time for - ", AlgorithmType.DYNAMIC.value, ": ", end - start)

    generate_images.display_image_with_best_path(list_image, AlgorithmType.BRUTE_FORCE)
    generate_images.display_image_with_best_path(list_image, AlgorithmType.DYNAMIC)
    generate_images.compare_both_methods(list_image)
