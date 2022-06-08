import tensorflow as tf
from numpy import float32

from Frontend import Frontend
from View import View


class Manipulation:
    def __init__(self, rgb_image, filename, manipulation):
        self.rgb_image = rgb_image
        self.filename = filename
        self.choice_of_manipulation = manipulation

    def grayscale(self):
        rgb_tensor = tf.convert_to_tensor(self.rgb_image, dtype=float32)
        grayscale_image = tf.image.rgb_to_grayscale(rgb_tensor)
        print(grayscale_image)
        if self.choice_of_manipulation == 1:
            View().view_tensor(grayscale_image)
            choice = Frontend().file_operations()
            if choice is True:
                View().save_image(grayscale_image, self.filename)
            return True
        return grayscale_image

    def black_and_white(self):
        image_data = tf.data.Dataset.from_tensor_slices(self.grayscale())
        for row in image_data:
            for col in row:
                if tf.math.greater(col, 125):
                    tf.math.multiply(col, 0)
                else:
                    tf.math.multiply(col, 0)
        # m = tf.multiply(self.grayscale(), 0)
        # View().view_tensor(image_data)
