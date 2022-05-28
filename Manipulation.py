import tensorflow as tf
from numpy import float32


class Manipulation:
    def __init__(self, rgb_image):
        self.rgb_image = rgb_image

    def grayscale(self):
        rgb_tensor = tf.convert_to_tensor(self.rgb_image, dtype=float32)

        print(self.rgb_image)