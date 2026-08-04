
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
            # Print leading spaces
            for j in range(self.size - i):
                print(" ", end="")
            
            # Print ascending numbers (1 to i)
            for j in range(1, i + 1):
                print(j, end="")
            
            # Print descending numbers (i-1 down to 1)
            for j in range(i - 1, 0, -1):
                print(j, end="")
            
            print()

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
        # BUGGY LINE : energy = self.energy - energy_loss
        # CORRECTED LINE: Updating self.energy directly
        self.energy = self.energy - energy_loss
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