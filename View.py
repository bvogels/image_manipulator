import PIL
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from Frontend import Frontend


class View:
    def view_image(self, image_path, manipulation):
        if manipulation == 3:
            image = PIL.Image.open(image_path)
        else:
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

    def save_image(self, image_as_array, filename, manipulation):
        m = {1: 'grayscale', 2: 'bw', 3: 'new_colors'}
        plt.imshow(image_as_array, cmap='gray')
        new_filename = filename[:8]
        plt.savefig(new_filename + m[manipulation])
        print(Frontend().messages(1) + "{}_{}".format(new_filename, m[manipulation]))
        plt.close()
