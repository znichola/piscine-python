# https://matplotlib.org/stable/tutorials/images.html

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    '''Invert the colors of the image received.'''
    return 255 - array  # this works using the broadcast from numpy


def ft_red(array: np.ndarray) -> np.ndarray:
    '''Isolate the red color channel of the image received.'''
    return array * [1, 0, 0]


def ft_green(array: np.ndarray) -> np.ndarray:
    '''Isolate the green color channel of the image received.'''

    def only_green(a, axis=0):
        '''Only green'''
        return np.array([a[0] - a[0], a[1], a[2] - a[2]])

    return np.apply_along_axis(only_green, 2, array)


def ft_blue(array: np.ndarray) -> np.ndarray:
    '''Isolate the blue color channel of the image received.'''

    def only_blue(a, axis=0):
        '''Only blue'''
        return np.array([0, 0, a[2]])

    return np.apply_along_axis(only_blue, 2, array)


def ft_grey(array: np.ndarray) -> np.ndarray:
    '''Convert to geryscale the image received.'''
    
    def only_grey(a, axis=0):
        '''Only grey'''
        # G*.59+R*.3+B*.11
        # r = a[0]
        # g = a[1]
        # b = a[2]

        # c = 1/(1/r/g/b)/(r/(g/b))

        # r = 510/a[0]
        # g = r/a[1]
        # b = g/a[2]

        return np.array([a[1], a[1], a[1]])

    return np.apply_along_axis(only_grey, 2, array)
