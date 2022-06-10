class Frontend:
    def main_menu(self):
        print("+" * 25)
        print("+++ Image Manipulator +++")
        print("+" * 25)
        print()
        print("(1) Select and view image (no manipulation)")
        print("(2) Manipulate an image")
        print("(3) Quit")
        choice = input("Choice: ")
        return int(choice)

    def basic_manipulations(self):
        print("Available manipulations:")
        print("(1) Convert to grayscale")
        print("(2) Convert to b/w")
        print("(3) Manipulate rgb color values")
        choice = input("Choice: ")
        return int(choice)

    def rgb_manipulation(self):
        print("Modify RGB values by entering percentage (0-100)")
        print("(Negative values will reduce color value)")
        red = float(input("Red: "))
        green = float(input("Green: "))
        blue = float(input("Blue: "))
        return [red, green, blue]

    def advanced_manipulations(self):
        print("Advanced manipulations")
        print("(1) Convert grayscale to b/w")
        print("(2) Manipulate rgb color values")
        choice = input("Choice: ")
        return int(choice)

    def miscellaneous(self):
        print("(1) Show advanced options")
        print("(2) Return to main menu")
        choice = input("Choice: ")
        return int(choice)

    def file_operations(self):
        choice = input("Do you want to save the image? (y/n) ")
        if choice == "y":
            return True
        else:
            return False

    def bw_treshold(self):
        choice = input("Do you want to customize the b/w treshold? (y/n)")
        if choice == "y":
            return True
        else:
            return False

    def messages(self, message):
        m = {1: "File saved to ",
             2: "B/w treshold is ",
             3: "This may take some time.",
             4: "Working on line "}
        return m[message]
