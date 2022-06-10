import tensorflow as tf
from PIL import Image
from tensorflow import float32

from Frontend import Frontend
from View import View


class Manipulation:
    def __init__(self, rgb_image, filename, manipulation):
        self.rgb_image = rgb_image
        self.filename = filename
        self.choice_of_manipulation = manipulation

    # This function grayscales an image. It uses the rgb_to_grayscale function
    # of TensorFlow.

    def grayscale(self):
        rgb_tensor = tf.convert_to_tensor(self.rgb_image, dtype=float32)
        grayscale_image = tf.image.rgb_to_grayscale(rgb_tensor)
        print(grayscale_image)
        if self.choice_of_manipulation == 1:
            View().view_tensor(grayscale_image)
            choice = Frontend().file_operations()
            if choice is True:
                View().save_image(grayscale_image, self.filename, self.choice_of_manipulation)
            return True
        return grayscale_image

    # This function converts an image to black and white.

    def black_and_white(self):
        custom_treshold = Frontend().bw_treshold()
        if custom_treshold:
            treshold = float32(input("Enter b/w treshold (0-255): "))
        else:
            treshold = 127.
        print(Frontend().messages(2), treshold)
        white = tf.ones_like(self.grayscale())
        black = tf.zeros_like(self.grayscale())
        bw = tf.where(tf.less(self.grayscale(), treshold), black, white)
        View().view_tensor(bw)
        choice = Frontend().file_operations()
        if choice is True:
            View().save_image(bw, self.filename, self.choice_of_manipulation)
        return True

    # This function changes the color values of an image.

    def adjust_rgb_values(self):
        new_color_values = Frontend().rgb_manipulation()
        r, g, b = self.rgb_image.split()
        r = r.point(lambda i: (255 - i) / 100 * new_color_values[0] if new_color_values[0] > 0 else i / 100 * new_color_values[0])
        g = g.point(lambda i: (255 - i) / 100 * new_color_values[1] if new_color_values[1] > 0 else i / 100 * new_color_values[1])
        b = b.point(lambda i: (255 - i) / 100 * new_color_values[2] if new_color_values[2] > 0 else i / 100 * new_color_values[2])
        rgb = Image.merge('RGB', (r, g, b))
        View().view_tensor(rgb)
        choice = Frontend().file_operations()
        if choice is True:
            View().save_image(rgb, self.filename, self.choice_of_manipulation)
        return True
