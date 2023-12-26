# https://matplotlib.org/stable/tutorials/images.html

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    '''Enhance! zoom into an image like it's a black and white CSI minami'''
    try:
        img = ft_load("../doc/animal.jpeg")

        final = img[125:125+400:, 450:450+400, 2:3]

        shape = np.shape(final)
        shape.count
        print(f"New shape after slicing: {shape}",
              f"or {(shape[0], shape[1])}" if shape[2] == 1 else "")
        print(final)
        plt.imshow(final, cmap="grey")
        plt.show()
    except Exception as e:
        print(f"Zoom fatal error: {e}")
        relaunch = input("Fix the image then retry (yes/no): ").lower()
        if relaunch == 'yes' or relaunch == 'y':
            main()
        else:
            print("Exiting the program.")


if __name__ == "__main__":
    main()
