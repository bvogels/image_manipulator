import os
from Frontend import Frontend
from Manipulation import Manipulation
from View import View


def traverse_images():
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
    f = Frontend()
    v = View()
    choice = f.main_menu()
    if choice == 1:
        image_choice = traverse_images()
        v.view_image(image_choice)
    elif choice == 2:
        image_choice = traverse_images()
        manipulation = f.manipulations()
        m = Manipulation(v.view_image(image_choice))
        m.grayscale()
    elif choice == 3:
        quit()
