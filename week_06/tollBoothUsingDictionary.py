class tollBooth:
    def __init__(self):
        self.total_amount = 0
        self.total_cars = 0
        self.reg_dict = {}

    def Total_amount(self):
        self.total_amount += 100

    def Total_cars(self):
        self.total_cars += 1

    def check_credit(self):
        reg_No = int(input("Enter Your registration No.: "))
        
        if reg_No in self.reg_dict:
            count = self.reg_dict[reg_No]
        else:
            count = 0

        # Check agar relaxation 5 times se kam hai
        if count < 5:
            self.reg_dict[reg_No] = count + 1
            self.Total_cars()  # Credit car ko bhi total cars me count kar liya
            print(f"Credit Allowed! Registration No {reg_No} has used {count + 1}/5 relaxations.")
        else:
            print(f"ALERT: Registration No {reg_No} has already used 5 relaxations! Payment Required.")

    def carPass(self, num):
        if num == 1:
            self.Total_amount()
            self.Total_cars()
            print(f"Total Amount Collected: {self.total_amount}")
            print(f"Total Cars Passed: {self.total_cars}")
        elif num == 2:
            self.check_credit()
        else:
            print("Invalid Input!")


toll1 = tollBooth()

while True:
    num = int(input("\n --------MENU-------- \n PRESS 1 IF YOU WANT TO PAY! \n PRESS 2 IF YOU WANT TO PAY LATER! \n PRESS ANY OTHER NUMBER IF YOU WANT TO EXIT \n"))

    if num != 1 and num != 2:
        print("Exiting Loop.....")
        break
    toll1.carPass(num)

# End me dictionary traverse karke summary print karna
print("\n--- All Credit Registration Records ---")
for reg_no, count in toll1.reg_dict.items():
    print(f"Registration Number -->> {reg_no} (Used: {count} times)")