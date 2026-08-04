# Local and Global Variable Error Varification:
a = 5
def fn():
    print("Hello!")     # Prints Hello!
    print(a)            # Error
    a = 7
print(a)
fn()

# -------------------------------------------------

# My_Account Class and Simple ATM Machine Functionallity using Methods:

class My_Account:
    def __init__(self, name, pin):
        self.Name = name
        self.PIN = pin
        self.__Balance = 0

    def withDrawAmount(self, enteredAmount):
        if enteredAmount <= 0:
            print("Invalid amount")
        elif enteredAmount > self.__Balance:
            print("Your Balance is less than Entered Amount")
        else:
            self.__Balance -= enteredAmount  
            print("Successful withdraw!")

    def depositeAmount(self, enteredAmount):
        if enteredAmount <= 0:
            print("Please Enter a positive number!")
        else:
            self.__Balance += enteredAmount
            print("Successful deposit")

    def showBalance(self):
        print(self.__Balance)


ac1 = My_Account("MF", 1234)

print("---------- MENU -----------")
print("PRESS 1 FOR BALANCE ENQUIRY")
print("PRESS 2 TO WITHDRAW MONEY")
print("PRESS 3 TO DEPOSIT MONEY")
print("PRESS 4 TO EXIT")

flag = True
while flag == True:
    num = int(input("please enter a number from menu to proceed : "))
    if num <= 0 :
        print("invalid number")
    elif num == 1:
        ac1.showBalance()
    elif num == 2:
       ac1.withDrawAmount(int(input("Enter Amount: ")))
    elif num == 3 :
        ac1.depositeAmount(int(input("Enter Amount: ")))
    elif num == 4:
        print("Thank You for using the ATM")
        flag = False

# ---------------------------------------------------------------

# Accessing Private Variables and Attributes Outside Class

# print(ac1.__Balance)               # Error Beacuse __Balanace is private

print(ac1._My_Account__Balance)      # Prints Balance of User Account

 