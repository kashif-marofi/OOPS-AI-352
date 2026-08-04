# Simple ATM Machine Functionality

print("--------MENU--------")
print("PRESS 1 FOR BALANCE ENQUIRY")
print("PRESS 2 TO WITHDRAW MONEY")
print("PRESS 3 TO DEPOSIT MONEY")
print("PRESS 4 TO EXIT")

userBalance = 50000
flag = True
while flag == True:
    num = int(input("please enter a number from menu to proceed : "))
    if num <= 0 :
        print("invalid number")
    elif num == 1:
        print("amount = ",userBalance,"Rs")
    elif num == 2:
        withdraw = int(input("please enter amount to withdraw : "))
        if withdraw <=0:
            print("Invalid amount")
        elif withdraw > userBalance:
            print("Insufficient Balance --- Your Balance = ", userBalance,"Rs")
        else:
            userBalance = userBalance - withdraw
            print("Successful withdraw")
            print("remaining Balance = ", userBalance,"Rs")
    elif num == 3 :
        deposit = int(input("please enter an amount to deposit : "))
        if deposit <=0 :
            print("Invalid amount ")
        else :
            userBalance = userBalance + deposit 
            print("Successful deposit")
            print("updated balance = ", userBalance,"Rs")
    elif num == 4:
        print("Thank You for using the ATM <3")
        flag = False

# Student

class Student:
    def __init__(self, name, age, marks, grade):
        self.name = name
        self.age = age
        self.marks = marks
        self.grade = grade

    def stdinfo(self):
        print(self.name, " is ", self.age, " years old ")
        print("he is in ", self.grade, "th grade and got ", self.marks, " marks out of 800 marks")

    def percent(self, marks):
        percentage = (self.marks / 800) * 100
        print(percentage, "%")


Std1 = Student("ballu", 16, 580, 8)
Std2 = Student("pappu", 17, 750, 9)
Std3 = Student("bhallay", 18, 690, 10)

Std1.stdinfo()
Std2.stdinfo()
Std3.stdinfo()

print("pappu got :")
Std2.percent(Std2.marks)
print("bhallay got :")
Std3.percent(Std3.marks)
print("ballu got :")
Std1.percent(Std1.marks)