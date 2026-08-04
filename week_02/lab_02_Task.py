# ASSIGNMENT: ATM WITHDRAWAL SYSTEM
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