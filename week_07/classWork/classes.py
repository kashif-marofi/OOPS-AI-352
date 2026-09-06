import math
class Shape:
    def __init__(self, color, isFilled = False):
        self.color = color
        self.isFilled = isFilled
    def fill_color(self):
        if self.isFilled == False:
            self.isFilled = True
    def show_info(self):
        print("Shape is not Defined!")

class Circle(Shape):
    def __init__(self, radius,  color, isFilled=False):
        super().__init__(color, isFilled)
        self.radius = radius
    def calc_Area(self):
        return math.pi * self.radius**2
    def calc_circum(self):
        return 2 * math.pi * self.radius
    def show_info(self):
        print(f"Circle with radius {self.radius} and color {self.color} and isFilled = {self.isFilled}")

class Square(Shape):
    def __init__(self, length,  color, isFilled=False):
        super().__init__(color, isFilled)
        self.length = length
    def calc_Area(self):
        return self.length**2
    def calc_circum(self):
        return 4 * self.length
    def show_info(self):
        print(f"Square with length {self.length} and color {self.color} and isFilled = {self.isFilled}")

class Rectangle(Shape):
    def __init__(self, length, bredth,  color, isFilled=False):
        super().__init__(color, isFilled)
        self.length = length
        self.bredth = bredth
    def calc_Area(self):
        return self.length * self.bredth
    def calc_circum(self):
        return 2 * self.length + 2 * self.bredth
    def show_info(self):
        print(f"Rectangle with length {self.length} and bredth {self.bredth} and color {self.color} and isFilled = {self.isFilled}")


class Triangle(Shape):
    def __init__(self, length, bredth,  color, isFilled=False):
        super().__init__(color, isFilled)
        self.length = length
        self.bredth = bredth
    def calc_Area(self):
        return 0.5 * self.length * self.bredth
    def show_info(self):
        print(f"Triangle with length {self.length} and bredth {self.bredth} and color {self.color} and isFilled = {self.isFilled}")
