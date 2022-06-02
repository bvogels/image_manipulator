import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class View:
    def view_image(self, image_path):
        image = mpimg.imread(image_path)
        plt.imshow(image)
        plt.show()
        return image

    def view_tensor(self, image_as_array):
        plt.imshow(image_as_array)
        plt.show()
