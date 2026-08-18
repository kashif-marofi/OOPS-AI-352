class Vehicle:
    def __init__(self, regist, v_type):
        self.regist = regist
        self.v_type = v_type

    def amountpaid(self):
        if self.v_type == 1:
            return 100
        elif self.v_type == 2:
            return 500
        return 0


class tollBooth:
    def __init__(self):
        self.total_amount = 0
        self.total_cars = 0
        self.vehicle_list = []  # Unpaid / Credit vehicles list

    def check_credit(self, v_obj):
        count = 0
        for item in self.vehicle_list:
            if item.regist == v_obj.regist:
                count += 1

        if count < 5:
            self.vehicle_list.append(v_obj)
            self.total_cars += 1
            print(f"Credit Allowed! Vehicle {v_obj.regist} has used {count + 1}/5 relaxations.")
        else:
            print(f"ALERT: Vehicle {v_obj.regist} has used 5 relaxations! Payment Required.")

    def carPass(self, num, v_obj):
        if num == 1:
            fee = v_obj.amountpaid()
            self.total_amount += fee
            self.total_cars += 1
            print(f"Fee Paid: RS {fee}")
        elif num == 2:
            self.check_credit(v_obj)
        else:
            print("Invalid Input!")


toll1 = tollBooth()

while True:
    num = int(input("\n--------MENU--------\nPRESS 1 IF YOU WANT TO PAY!\nPRESS 2 IF YOU WANT TO PAY LATER!\nPRESS ANY OTHER NUMBER TO EXIT\nChoice: "))

    if num != 1 and num != 2:
        print("Exiting Loop.....")
        break

    reg_no = int(input("Enter Registration No.: "))
    v_type = int(input("Enter Vehicle Type (1 for Normal [100 RS], 2 for Heavy [500 RS]): "))

    v_obj = Vehicle(reg_no, v_type)
    toll1.carPass(num, v_obj)


print("\n================ AT THE END ================")

# 1. How much amount is collected
print(f"1. Total Amount Collected: RS {toll1.total_amount}")

# 3. How many cars have passed
print(f"2. Total Cars Passed: {toll1.total_cars}")

# 2. List of all vehicles that have not paid
print("\n3. List of Vehicles That Have Not Paid (Credit):")
if not toll1.vehicle_list:
    print("   None")
else:
    for obj in toll1.vehicle_list:
        v_name = "Normal" if obj.v_type == 1 else "Heavy"
        print(f"   Registration No: {obj.regist} | Type: {v_name}")

# 4. List according to type
print("\n4. Unpaid Vehicles Categorized By Type:")
print("   --- Normal Vehicles ---")
for obj in toll1.vehicle_list:
    if obj.v_type == 1:
        print(f"   Registration No: {obj.regist}")

print("   --- Heavy Vehicles ---")
for obj in toll1.vehicle_list:
    if obj.v_type == 2:
        print(f"   Registration No: {obj.regist}")

# 5. Total unpaid amount
unpaid_total = 0
for obj in toll1.vehicle_list:
    unpaid_total += obj.amountpaid()

print(f"\n5. Total Unpaid Amount: RS {unpaid_total}")
print("============================================")