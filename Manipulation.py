import tensorflow as tf
from numpy import float32

from Frontend import Frontend
from View import View


class Manipulation:
    def __init__(self, rgb_image, filename):
        self.rgb_image = rgb_image
        self.filename = filename

    def grayscale(self):
        rgb_tensor = tf.convert_to_tensor(self.rgb_image, dtype=float32)
        grayscale_image = tf.image.rgb_to_grayscale(rgb_tensor)
        View().view_tensor(grayscale_image)
        choice = Frontend().file_operations()
        if choice is True:
            View().save_image(grayscale_image, self.filename)
        return True
