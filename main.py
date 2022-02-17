# grid attribute is a list of lists
def print_grid(grid):
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print(" ---  --- ---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print(" ---  --- ---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")

print("Welcome to My Minimalistic Game of Tic Tac Toe!")

# Players
players = [{"name": "Player 1", "symbol": "X"},
           {"name": "Player 2", "symbol": "O"}]

# All grid values into empty strings
# a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = " "

# Initialize all grid values into its grid position string
# a1, a2, a3, b1, b2, b3, c1, c2, c3 = 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'

# Values in grid in list of lists
# grid = [[a1, a2, a3],
#         [b1, b2, b3],
#         [c1, c2, c3]]

grid = [['A1', 'A2', 'A3'],
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3']]

# Loop
print(f"{players[0]['name']} ('{players[0]['symbol']}') turn.")
print(f"Please choose the grid position where you want to place... ")
print()

# Print grid format with grid columns
# print("    1   2   3")
# print(f" A  {a1} | {a2} | {a3}")
# print("   --- --- ---")
# print(f" B  {b1} | {b2} | {b3}")
# print("   --- --- ---")
# print(f" C  {c1} | {c2} | {c3}")

# Print grid format without grid columns
print_grid(grid)

print()

# Chosen Grid Position
player_move = input("").upper()

# Check if Pos Exists
gridpos_exists = any(player_move in moves for moves in grid)
print(f"Position exists: {gridpos_exists}")

if gridpos_exists:
    row_index = [i for i, lst in enumerate(grid) if player_move in lst][0]
    # print(f"Row Grid Index: {row_index}")
    column_index = grid[row_index].index(player_move)
    # print(f"Column Grid Index: {column_index}")

    grid[row_index][column_index] = players[0]['symbol']

print_grid(grid)
