from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Load image from path into numpy.ndarray'''
    try:
        img = np.asarray(Image.open(path))
        final = img[125:125+400:, 450:450+400, 2:3]
        print(f"The shape of image is: {np.shape(final)}")
        print(final)
        return final
    except Exception as e:
        print(f"ft_load fatal error: {e}")
        raise
