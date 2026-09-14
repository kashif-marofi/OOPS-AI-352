class HEI:
    total_budget = 10000000 

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.faculty_members = [] 

    def calculate_remuneration(self):
        return 0

    def add_faculty(self, faculty):
        rem = faculty.calculate_remuneration()

        if rem > HEI.total_budget:
            print(f"\n Budget insufficient! Cannot add {faculty.name}.")
            print(f"Required: Rs. {rem:,} | Remaining Budget: Rs. {HEI.total_budget:,}")
            return False
        else:
            HEI.total_budget -= rem
            self.faculty_members.append(faculty)
            print(f" {faculty.name} added successfully!")
            print(f"Remuneration: Rs. {rem:,}")
            print(f"Remaining Budget: Rs. {HEI.total_budget:,}")
            return True

    def display_all(self):
        print("\n" + "="*45)
        print(f"      {self.name} - REMUNERATION REPORT")
        print("="*45)
        
        visiting_total = 0

        # Polymorphism
        for f in self.faculty_members:
            rem = f.calculate_remuneration()
            print(f"ID: {f.id} | Name: {f.name} | Remuneration: Rs. {rem:,}")
            
            # Visiting / Part_Time remuneration tracking
            if isinstance(f, Part_Time):
                visiting_total += rem

        print("-" * 45)
        print(f"Total Remuneration Paid to Visiting Faculty: Rs. {visiting_total:,}")
        print(f"Final Remaining Budget: Rs. {HEI.total_budget:,}")
        print("="*45)


class Full_Time(HEI):
    
    designation_dict = {
        1: ("Lecturer", 50000),
        2: ("Assistant Professor", 75000),
        3: ("Associate Professor", 150000),
        4: ("Professor", 225000)
    }

    def __init__(self, name, id):
        super().__init__(name, id)
        self.base_pay = 75000
        self.allowance = 0
        self.designation_name = ""

    def check_designation(self):
        print("\nEnter a number according to your designation:  ")
        print("1. Lecturer  ")
        print("2. Assistant Professor ")
        print("3. Associate Professor ")
        print("4. Professor ")
        
        choice = int(input("Select designation (1-4): "))
        if choice in Full_Time.designation_dict:
            self.designation_name, self.allowance = Full_Time.designation_dict[choice]
        else:
            print("Invalid choice! Setting default as Lecturer.")
            self.designation_name, self.allowance = Full_Time.designation_dict[1]

    # Method Overriding
    def calculate_remuneration(self):
        return self.base_pay + self.allowance


class Part_Time(HEI):
    
    visiting_dict = {
        1: ("Industry Professional", 2500),
        2: ("Interdepartmental Teacher", 1500)
    }

    def __init__(self, name, id, total_hours):
        super().__init__(name, id)
        self.total_hours = total_hours
        self.rate_per_hour = 1000
        self.visiting_type = ""

    def check_visiting_type(self):
        print("\nSelect Visiting Faculty Type:")
        print("1. Industry Professional")
        print("2. Interdepartmental Teacher")
        
        choice = int(input("Select type (1-2): "))
        if choice in Part_Time.visiting_dict:
            self.visiting_type, self.rate_per_hour = Part_Time.visiting_dict[choice]
        else:
            print("Invalid choice! Setting default rate (1000).")

    # Method Overriding
    def calculate_remuneration(self):
        return self.total_hours * self.rate_per_hour


institute = HEI("Karachi University", "KU-001")

while True:
    print("\n--- ENTER FACULTY TYPE ---")
    print("1. Full Time")
    print("2. Part Time")
    print("3. Exit and Show Final Output")
    
    type_choice = input("Enter choice (1-3): ")

    if type_choice == '1':
        name = input("Enter Name: ")
        f_id = input("Enter ID: ")
        
        # Call Full_Time
        ft = Full_Time(name, f_id)
        # Call check_designation method
        ft.check_designation()
        # Add to HEI collection
        institute.add_faculty(ft)

    elif type_choice == '2':
        name = input("Enter Name: ")
        f_id = input("Enter ID: ")
        hours = int(input("Enter Total Hours: "))
        
        # Call Part_Time
        pt = Part_Time(name, f_id, hours)
        # Check for visiting and industry
        pt.check_visiting_type()
        # Add to HEI collection
        institute.add_faculty(pt)

    elif type_choice == '3':
        break
    else:
        print("Invalid choice, try again!")

# Final Report
institute.display_all()