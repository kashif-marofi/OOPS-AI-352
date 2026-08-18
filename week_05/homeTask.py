class Shapes:
    SHAPE_NAMES = {
        3: "Triangle",
        4: "Square",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon"
    }

    def __init__(self, sides, length, color, filled=False):
        self.sides = sides
        self.length = length
        self.color = color
        self.filled = filled

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, val):
        if 3 <= val <= 8:
            self.__sides = val
        else:
            self.__sides = None

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        self.__length = val

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        self.__color = val

    @property
    def filled(self):
        return self.__filled

    @filled.setter
    def filled(self, val):
        self.__filled = val


    def show_info(self):
        shape_name = self.SHAPE_NAMES.get(self.sides, "Invalid shape (Sides must be between 3 and 8)")
        
        if self.sides in self.SHAPE_NAMES:
            print(f"It is a {shape_name}, has sides: {self.sides}, length: {self.length}, color: {self.color}, filled: {self.filled}")
        else:
            print(shape_name)



shapes_list = []
n = int(input("Enter number of shapes: "))

for i in range(n):
    print(f"\n--- Shape {i + 1} ---")
    side = int(input("Enter sides (3 to 8): "))
    length = int(input("Enter length: "))
    color = input("Enter color: ")
    filled = input("Is it filled? (True/False): ")
    
    s = Shapes(side, length, color, filled)
    shapes_list.append(s)

print("\n=== SHAPES INFORMATION ===")
for shape in shapes_list:
    shape.show_info()