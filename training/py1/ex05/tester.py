from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


print(ft_invert.__doc__)


def main():
    '''Enhance! zoom into an image like it's a black and white CSI minami'''
    try:
        array = ft_load("../doc/landscape.jpg")

        # img = ft_invert(array)
        # img = ft_red(array)
        # img = ft_green(array)
        # img = ft_blue(array)
        img = ft_grey(array)

        print(img)
        plt.imshow(img)
        plt.show()
    except Exception as e:
        print(f"Image processing fatal error: {e}")
        relaunch = input("Fix the image then retry (yes/no): ").lower()
        if relaunch == 'yes' or relaunch == 'y':
            main()
        else:
            print("Exiting the program.")


if __name__ == "__main__":
    main()
