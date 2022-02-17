print("Welcome to My Minimalistic Game of Tic Tac Toe!")

# Players
player_1 = ("Player 1", "X")
player_2 = ("Player 2", "O")

# Loop
print(f"{player_1[0]} ({player_1[1]}) turn.")
print(f"Please choose the grid position where you want to place... ")

player_1_move = input("")

# All grid values into empty strings
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = " "

# Values in grid in list of lists
grid = [[a1, a2, a3],
        [b1, b2, b3],
        [c1, c2, c3]]

# Print grid format

print("    1   2   3")
print(f" A  {a1} | {a2} | {a3}")
print("   --- --- ---")
print(f" B  {b1} | {b2} | {b3}")
print("   --- --- ---")
print(f" C  {c1} | {c2} | {c3}")
