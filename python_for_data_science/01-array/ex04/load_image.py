from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Load image from path into numpy.ndarray and reshape'''
    try:
        img = np.asarray(Image.open(path))
        final = img[125:125+400:, 450:450+400, 2:3]
        shape = np.shape(final)
        print(f"New shape after slicing: {shape}",
              f"or {(shape[0], shape[1])}" if shape[2] == 1 else "")
        print(final)
        return final
    except Exception as e:
        print(f"ft_load fatal error: {e}")
        raise
