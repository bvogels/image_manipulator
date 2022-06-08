import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from Frontend import Frontend


class View:
    def view_image(self, image_path):
        image = mpimg.imread(image_path)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        return image

    def view_tensor(self, image_as_array):
        plt.imshow(image_as_array, cmap='gray')
        plt.axis('off')
        plt.show()
        return

    def save_image(self, image_as_array, filename):
        plt.imshow(image_as_array, cmap='gray')
        new_filename = filename[:8]
        plt.savefig(new_filename + "_bw")
        print(Frontend().messages(1) + "_bw".format(new_filename))
        plt.close()

