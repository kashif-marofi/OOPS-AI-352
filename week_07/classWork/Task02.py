from classes import Shape, Circle, Square, Rectangle, Triangle

n = int(input("Enter the number of shapes you want to insert! "))
total_Area = 0
total_Circum = 0
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

    if obj.isFilled == True:
        current_Area = obj.calc_Area()
        total_Area += current_Area
    else:
        current_Circum = obj.calc_circum()
        total_Circum += current_Circum

# print(f"Total Area is {total_Area}")
# print(f"Total Circumference is {total_Circum}")
print(total_Area + total_Circum)