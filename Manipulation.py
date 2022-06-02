import tensorflow as tf
from numpy import float32

from View import View


class Manipulation:
    def __init__(self, rgb_image):
        self.rgb_image = rgb_image

    def grayscale(self):
        rgb_tensor = tf.convert_to_tensor(self.rgb_image, dtype=float32)
        grayscale_image = tf.image.rgb_to_grayscale(rgb_tensor)
        print(rgb_tensor)
        print(grayscale_image)
        View().view_tensor(grayscale_image)