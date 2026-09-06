class Account:
    def __init__(self, title, acc_No):
        self.Title = title
        self.Acc_No = acc_No
        self.__Balance = 0
    @property
    def balance(self):
        return self.__Balance
    balance.setter
    def balance(self, value):
        print("Setter for Balance!")
    
    def withDrawAmount(self, title, acc_no, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__Balance:
            print("Your Balance is less than Entered Amount")
        else:
            self.__Balance -= amount  
            print("Successful withdraw!")
    
    def depositeAmount(self, title, acc_no, amount):
        if amount <= 0:
            print("Please Enter a positive number!")
        else:
            self.__Balance += amount
            print("Successful deposit")
    
    def showBalance(self):
        print(self.__Balance)

class Current_Account(Account):
    def __init__(self, withdraw_Amount):
        super().__init__()
        self.Withdraw_Amount = withdraw_Amount

class Saving_Account(Account):
    def __init__(self):
        super().__init__()

class Bank:
    def __init__(self, name):
        self.Accounts_List = []
        