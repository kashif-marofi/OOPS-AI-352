class FB_Player :
    def __init__ (self, name, team, position):
        self.Name = name
        self.Team = team
        self.Position = position
        self.Score = 0
    
    def updateScore(self, score):
        self.Score += score
    
    def showInfo(self):
        print(f"{self.Name} is player of {self.Team}, play at position {self.Position}, and has score {self.Score}")

    def compare(p1 , p2):
        if p1.Score > p2.Score:
            print(f"{p1.Name} is better than {p2.Name}")
        elif p1.Score == p2.Score:
            print("Both Players are equal")
        else:
            print(f"{p2.Name} is better than {p1.Name}")

# # ----------------------------------------------------------------------------


# # # Global/Outer Compare Function

def compare(p1 , p2):
        if p1.Score > p2.Score:
            print(f"{p1.Name} is better than {p2.Name}")
        elif p1.Score == p2.Score:
            print("Both Players are equal")
        else:
            print(f"{p2.Name} is better than {p1.Name}")

p1 = FB_Player("Rodri", "Spain", "CDM")
p2 = FB_Player("Naymar", "Brazil", "RW")
print(p1.showInfo())

# updateScore() 
p1.updateScore(20)
p2.updateScore(25)

# showInfo()
p1.showInfo()
p2.showInfo()


# Comper Call as an outer function
compare(p1,p2)

# Comper Call as Class inner function
FB_Player.compare(p1, p2)

# # -------------------------------------------------------

p1 = FB_Player("Rodri", "Spain", "CDM")
p2 = p1
p3 = FB_Player("Naymar", "Brazil", "RW")
p1 = p3

p1.updateScore(20)
p2.updateScore(25)


print(p2 == p1)
print(p2.Name == p1.Name)
print(p2.Team == p1.Team)
print(p2.Position == p1.Position)
print(p2.Score == p1.Score)

print(p1.Name)
print(p2.Name)
print(p3.Name)


# -------------------------------------------------------------

# How to get Ref/address of a variable:

a = 10

address_in_interger = id(a)
address_in_hexadecimal = hex(id(a))

print(f"Address in integer: {address_in_interger}")
print(f"Address in Hexademial: {address_in_hexadecimal}")


# -------------------------------------------------------------------------------
# Pattern Assognment:
# Print this Pattern:

#            *
#          * * *
#        * * * * *
#      * * * * * * *     OR FOR NUMBERS INSTEAD OF STARS

# #  Upper Hill

n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end = " ")
    for j in range(1, i + 1):
        print( j, end = " ")
    for j in range(i - 1 , 0 , -1):
        print(j , end = " ")
    print()