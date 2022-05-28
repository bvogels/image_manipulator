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

    def manipulations(self):
        print("Available manipulations:")
        print("(1) Convert to grayscale")
        print("(2) Convert to b/w")
        choice = input("Choice: ")
        return int(choice)