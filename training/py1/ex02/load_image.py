from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Load image from path into numpy.ndarray'''
    try:
        img = np.asarray(Image.open(path))
        print(f"The shape of image is: {np.shape(img)}")
        print(img)
        return img
    except Exception as e:
        print(f"ft_load fatal error: {e}")
        raise
