import os
from Frontend import Frontend
from Manipulation import Manipulation
from View import View


# This function traverses the res directory, thus collecting the names of
# all files. The filenames are then displayed in an indexed lists. The files
# can be accessed by their index.

def traverse_gallery():
    directory = 'res'
    images = {}
    index = 1
    for image in os.listdir(directory):
        file = os.path.join(directory, image)
        if os.path.isfile(file):
            images[index] = file
            index += 1
    print("+" * 34)
    print("+++ No. ++ Name ++++++++++++++++++")
    print("+" * 34)
    for index in images.keys():
        print("+   {}   +  {}".format(index, images[index][4:]))
    print("+" * 34)
    img = input("Choice: ")
    return images[int(img)]


if __name__ == "__main__":
    while True:
        choice = Frontend().main_menu()
        if choice == 1:
            image_choice = traverse_gallery()
            View().view_image(image_choice, choice)
        elif choice == 2:
            image_choice = traverse_gallery()
            manipulation = Frontend().basic_manipulations()
            if manipulation == 1:
                m = Manipulation(View().view_image(image_choice, manipulation), image_choice, manipulation)
                m.grayscale()
            elif manipulation == 2:
                m = Manipulation(View().view_image(image_choice, manipulation), image_choice, manipulation)
                m.black_and_white()
            elif manipulation == 3:
                m = Manipulation(View().view_image(image_choice, manipulation), image_choice, manipulation)
                m.adjust_rgb_values()
        elif choice == 3:
            quit()
