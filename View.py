import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class View:
    def view_image(self, image_path):
        image = mpimg.imread(image_path)
        plt.imshow(image)
        plt.show()
        return image
