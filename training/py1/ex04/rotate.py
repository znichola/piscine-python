# https://matplotlib.org/stable/tutorials/images.html

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    '''Enhance! zoom into an image like it's a black and white CSI minami'''
    try:
        img = ft_load("../doc/animal.jpeg")
        print("--------")

        final = img.squeeze()
        print(f"shape {final.shape}")
        shape = np.shape(final)
        n = np.empty((shape[1], shape[0]))
        for i, a in enumerate(final):
            for j, b in enumerate(a):
                n[j][i] = b
        final = n
        # final = final.transpose(1, 0)
        shape = np.shape(final)
        shape.count
        print(f"New shape after Transpose: {shape}")
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
