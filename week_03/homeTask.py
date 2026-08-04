# -------------------------------------------------------------------------------
# Print this Pattern:
#            *
#          * * *
#        * * * * *
#      * * * * * * *     OR FOR NUMBERS INSTEAD OF STARS
#        * * * * *
#          * * *
#            *

# #  Upper Hill
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i + 1):
        print("*" , end = " ")
    print()

# # Lower Hill
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n - i):
        print("*", end = " ")
    for j in range(n - i - 1):
        print("*", end =" ")  
    print()



# #  Full Diamond Pattern(Stars)
n = 5
for i in range(n - 1):
    for j in range(i, n):
        print(" ", end = " ")
    for j in range(i):
        print("$", end = " ")
    for j in range(i + 1):
        print("#" , end = " ")
    print()
    
for i in range(n):
    for j in range(i + 1):
        print(" ", end = " ")
    for j in range(n - i):
        print("*", end = " ")
    for j in range(n - i - 1):
        print("*", end =" ")  
    print()


# # Full Diamond Pattern of Numbers:
n = 5
for i in range(n - 1):
    for j in range(i, n):
        print(" ", end = " ")
    for j in range(1, i + 1):
        print( j, end = " ")
    for j in range(i - 1 , 0 , -1):
        print(j , end = " ")
    print()
    
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end = " ")
    for j in range(1, i + 1):
        print(j , end = " ")
    for j in range(i - 1, 0, -1):
        print(j , end =" ")  
    print()


# Assignment : 01
class PatternBuilder:
    def __init__(self, symbol, size):
        self.symbol = symbol
        self.size = size

    def draw_hollow_square(self):
        print("Hollow Square:")
        for r in range(self.size):
            for c in range(self.size):
                # Boundary conditions for hollow square
                if r == 0 or r == self.size - 1 or c == 0 or c == self.size - 1:
                    print(self.symbol, end=" ")
                else:
                    print(" ", end=" ")
            print()

    def draw_number_pyramid(self):
        print("\nNumber Pyramid:")
        for i in range(self.size, 0, -1):
            # Print leading spaces for alignment
            spaces = " " * (self.size - i)
            
            # Construct ascending sequence (1 to i)
            asc = [str(x) for x in range(1, i + 1)]
            # Construct descending sequence (i-1 down to 1)
            desc = [str(x) for x in range(i - 1, 0, -1)]
            
            row_str = "".join(asc + desc)
            print(spaces + row_str)

# Testing Task 1
builder = PatternBuilder(symbol="*", size=4)
builder.draw_hollow_square()
builder.draw_number_pyramid()



# Assignment : 02

class Sprinter:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def run_stage(self, miles):
        energy_loss = miles * 2
        # BUGGY LINE WAS: energy = self.energy - energy_loss
        # CORRECTED LINE: Updating instance variable self.energy directly
        self.energy = self.energy - energy_loss
        # Explanation: Buggy line created a temporary local variable named 'energy' 
        # that disappeared after run_stage finished. Using 'self.energy' updates 
        # the persistent attribute belonging to the instance object.
        print(f"{self.name} completed the stage.")

    def view_stats(self):
        print(f"{self.name}'s current energy: {self.energy}")

# Testing Task 2
runner = Sprinter("Bolt")
runner.run_stage(15)
runner.view_stats()  # Output: Bolt's current energy: 70


# Assignment : 04

import random

class Batsman:
    def __init__(self, name):
        self.name = name
        self.runs_scored = 0

    def score_runs(self, runs):
        self.runs_scored += runs

# Simulation logic
batsman = Batsman("Babar Azam")
possible_runs = [0, 1, 2, 3, 4, 6]

print(f"--- Super Over Simulation for {batsman.name} ---")
for ball in range(1, 7):
    runs_on_ball = random.choice(possible_runs)
    batsman.score_runs(runs_on_ball)
    print(f"Ball {ball}: {runs_on_ball} runs scored")

print("-----------------------------------")
print(f"Final Score for {batsman.name}: {batsman.runs_scored} runs in 6 balls.")