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

    def file_operations(self):
        choice = input("Do you want to save the image? (y/n) ")
        if choice == "y":
            return True
        else:
            return False


    def messages(self, message):
        m = {1: "File saved to {}"}
        return m[message]