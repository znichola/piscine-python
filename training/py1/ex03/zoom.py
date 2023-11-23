from load_image import ft_load
import matplotlib.pyplot as plt


if __name__ == "__main__":
    try:
        img = ft_load("../doc/animal.jpeg")

        # print(img)

        imgplot = plt.imshow(img)
    except Exception as e:
        print(f"there seems to have been a fatal issue: {e}")
