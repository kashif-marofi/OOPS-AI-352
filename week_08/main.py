from classes import Account, Current_Account, Saving_Account, Bank

ac1 = Account("MF", 1234)
bank = Bank("UBL")
print("---------- HOME -----------")
print("1) Open an Account")
print("2) Delete an account")
print("3) Withdraw an amount")
print("4) Deposite an amount")
print("5) List of Accounts")
print("6) Transaction history of an account")
print("7) Total Withdrawl amount")
print("8) Total deposite amount")
print("9) EXIT")

flag = True
while flag == True:
    num = int(input("Please enter a number to proceed : "))
    if num <= 0 :
        print("invalid number")
    elif num == 1:
        title = input("Enter Title: ")
        acc_no = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount: "))
        obj1 = Account(title, acc_no)
        bank.Accounts_List.append(obj1)
        print("Congratulations for Opening new Account!")
    elif num == 2:
       acc_no = int(input("Enter Account Number: "))
       print("For Delete Account")
    elif num == 3 :
        title = input("Enter Title: ")
        acc_no = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount: "))
        ac1.withDrawAmount(title, acc_no, amount)
    elif num == 4:
        title = input("Enter Title: ")
        acc_no = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount: "))
        ac1.depositeAmount(title, acc_no, amount)
    elif num == 5:
        print("--- List of Accounts ---")
        for acc in bank.Accounts_List:
            print(f"Title: {acc.Title} Account No: {acc.Acc_No}")
    elif num == 6:
        print("Transaction History of Accounts")
    elif num == 7:
        print("Total Withdrawl amount")
    elif num == 8:
        print("Total Deposite amount")
    elif num == 9:
        print("Thank You for using the Bank")
        flag = False
