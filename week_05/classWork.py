# Area and Circumfrance of Circle 

# class Circle :
#     def __init__ (self, rad, color,):
#         self.rad = rad
#         self.color = color

#     def calculate_Area(self):
#         area = 3.142 * self.rad ** 2
#         print(f"Area of Circle:  {area}")
#     def calculate_Circum(self):
#         circum = 2 * 3.142 * self.rad
#         print(f"Area of Circle:  {circum}")

# c1 = Circle(int(input("Radius: ")), input("color: "))
# c1.calculate_Area()
# c1.calculate_Circum()


# Multiple defs of __init:

# class Square:
#     def __init__(self, s, l, c, f):
#         self.__side = s
#         self.len = l
#         self.col = c
#         self.filled = f

#     def __init__(self, s, l, c, f = False):       # This latest fn() always run
#             self.__side = s
#             self.len = l
#             self.col = c
#             self.filled = f
#     def info(self):
#          print(f"This shape has {self.__side} sides, and has length {self.len}, and its color is {self.col}, and FIlled {self.filled}")        

# obj1 = Square(4, 5, "red", True)
# obj2 = Square(4, 5, "red")
# obj1.info()
# obj2.info()

# Function Overloading:

# def fn(a, b):
#     return a + b
# def fn(a, b, c):        # As there is no fn() overloading in Python by default so the latest fn() will run
#     return a + b + c

# # fn(1,2)       # Error: 3 arguments are required???
# print(fn(1,2,3))

# List of Shapes:

class Shapes:
    def __init__(self, s, l, c, f = False):
        self.__side = s
        self.len = l
        self.col = c
        self.filled = f

    def show_Info(self,):
        if self.__side < 3 or self.__side > 8:
            print("Invalid input")
        elif self.__side == 3:
            print(f"It is a Triangle, has side: {self.__side} , and length is {self.len}, of color: {self.col}")
        elif self.__side == 4:
            print(f"It is a Square, has side: {self.__side} , and length is {self.len}, of color: {self.col}")
        elif self.__side == 5:
            print(f"It is a Pentagon, has side: {self.__side} , and length is {self.len}, of color: {self.col}")
        elif self.__side == 6:
            print(f"It is a Hexagon, has side: {self.__side} , and length is {self.len}, of color: {self.col}")
        elif self.__side == 7:
            print(f"It is a Heptagon, has side: {self.__side} , and length is {self.len}, of color: {self.col}")
        elif self.__side == 8:
            print(f"It is a Octagon, has side: {self.__side} , and length is {self.len}, of color: {self.col}")

o_l = []
n = int(input("Enter a number: "))
for i in range(n):
    side = int(input(f"Sides of shape {i + 1}: "))
    length = int(input(f"Length of shape {i + 1}: "))
    color = input(f"Color of shape {i + 1}: ")
    filled = input(f"FIlled of shape {i + 1}:")
    s = Shapes(side, length, color, filled)
    o_l.append(s)
for i in o_l:
    i.show_Info()  

# Properties:

# class Shapes:
#     def __init__(self, s, l):
#         self.__sides = s 
#         self.length = l

#     @property
#     def sides(self):
#         return self.__sides
#     @sides.setter
#     def sides(self, val):
#         self.__sides = val
#     @property
#     def length(self):
#         return self._length
#     @length.setter
#     def length(self, val):
#         self._length = val
#     @property
#     def area(self):
#         return self._length * 2
    
# side = int(input(f"Sides: "))
# length = int(input(f"Length : "))
# s = Shapes(side, length)
# print(s.sides)
# print(s.length)