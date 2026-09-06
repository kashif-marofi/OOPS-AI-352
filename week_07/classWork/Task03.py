from classes import Shape, Circle, Square, Rectangle, Triangle

n = int(input("Enter the number of shapes you want to insert! "))
total_Circles = 0
total_Squares = 0
total_Rectangles = 0
total_Triangles = 0
total_Filled = 0
total_Unfilled = 0
total_Shapes = []
for i in range(n):
   
    choice = int(input("Enter your Choice! \n 1 For Circle \n 2 For Square \n 3 For Rectangle \n 4 For Triangle \n"))
    if choice == 1:
        obj = Circle(5, "red")
    elif choice == 2:
        obj = Square(6, "green")
    elif choice == 3:
        obj = Rectangle(5, 6, "Blue", True)
    elif choice == 4:
        obj = Triangle(6, 7, "Yellow", True)
    else:
        print("Invalid Input!")

    total_Shapes.append(obj)

    # By using type() Function

        # if type(obj).__name__ == "Circle":
    #     total_Circles += 1
    # elif type(obj).__name__ == "Square":
    #     total_Squares += 1
    # elif type(obj).__name__ == "Rectangle":
    #     total_Rectangles += 1
    # elif type(obj).__name__ == "Triangle":
    #     total_Triangles += 1
    # else:
    #     print("Type nahi Milli!")

    # By using isinstance Methode

    if isinstance(obj, Circle):
        total_Circles += 1
    elif isinstance(obj, Square):
        total_Squares += 1
    elif isinstance(obj, Rectangle):
        total_Rectangles += 1
    elif isinstance(obj, Triangle):
        total_Triangles += 1
    else:
        print("Type nahi Milli!")

    if obj.isFilled == True:
        total_Filled += 1
    else:
        total_Unfilled += 1

print(f"Total Shapes are : {len(total_Shapes)}")
print(f"Total Circles : {total_Circles}")
print(f"Total Squares : {total_Squares}")
print(f"Total Rectangles : {total_Rectangles}")
print(f"Total Triangles : {total_Triangles}")
print(f"Total Filled : {total_Filled}")
print(f"Total Unfilled : {total_Unfilled}")