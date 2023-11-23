from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Load image from path'''
    try:
        img = np.asarray(Image.open(path))
        print(f"The shape of image is: {np.shape(img)}")
        return img
    except Exception as e:
        raise ValueError(f"ft_load error: {e}")
