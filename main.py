# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Box:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        pass
    def remove_tool(self):
        pass
    def show_inventory(self):
        for tool in self.tools:
            print(self.tools[tool])

class Tournevis:
    def __init__(self, size):
        self.size = size

    def tighten(self):
        pass
    def loosen(self):
        pass

class Marteau:
    def __init__(self, color="red"):
        self.color = color

    @classmethod
    def change_color(self, color):
        self.color = color
    def hammer_in(self, nail):
        pass
    def remove_nail(self, nail):
        pass


tournevis1 = Tournevis(1)
tournevis2 = Tournevis(2)
tournevis3 = Tournevis(3)
marteau1 = Marteau("blue")
marteau2 = Marteau
box = Box
box.add_tool(tournevis1)
box.add_tool(marteau2)
box.add_tool(marteau2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
