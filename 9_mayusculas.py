class String():
    def __init__(self):
        self.string1 = ""

    def get_string(self):
        self.string1 = input()

    def print_string(self):
        print(self.string1.upper())

str1 = String()
str1.get_string()
str1.print_string()
