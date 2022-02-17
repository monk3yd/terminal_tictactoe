# FUNCTIONS
# grid attribute is a list of lists
def print_grid(grid):
    print()
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print(" ---  --- ---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print(" ---  --- ---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")
    print()


# player is a dict and grid is a list of lists
def validate_answer(player, grid, move):
    # Check if Pos Exists
    gridpos_exists = any(move in moves for moves in grid)
    # print(f"Position exists: {gridpos_exists}")

    if gridpos_exists:
        row_index = [i for i, lst in enumerate(grid) if move in lst][0]
        column_index = grid[row_index].index(move)
        grid[row_index][column_index] = player['symbol']
        return grid
    else:
        print("Grid Position doesn't exists or it have already been played in this match.\nPlease enter a valid grid position value.")


def check_for_winner(grid):
    if grid[0][0] == grid[1][0] == grid[2][0] or grid[0][1] == grid[1][1] == grid[2][1] or grid[0][2] == grid[1][2] == grid[2][2]:
        print("Vertical Winner!")
        return True
    elif grid[0][0] == grid[0][1] == grid[0][2] or grid[1][0] == grid[1][1] == grid[1][2] or grid[2][0] == grid[2][1] == grid[2][2]:
        print("Horizontal Winner!")
        return True
    elif grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
        print("Diagonal Winner!")
        return True
    else:
        print("No winner yet!")
        return False


# MAIN
print("Welcome to My Minimalistic Game of Tic Tac Toe!")

# Players
players = [{"name": "Player 1", "symbol": "X"},
           {"name": "Player 2", "symbol": "O"}]


grid = [['A1', 'A2', 'A3'],
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3']]

# Control Flow
is_winner = False
turns = 9
i = 0  # Player 1 = 0 & Player 2 = 1

# Loop
while turns != 0 and is_winner is False:
    if turns % 2 != 0:
        i = 0
    else:
        i = 1

    print(f"It's {players[i]['name']} turn ('{players[i]['symbol']}').")

    # Print grid format without grid columns
    print_grid(grid)

    # Chosen Move Position
    player_move = input(f"Please {players[i]['name']} choose the grid position where you want to play...\n").upper()

    # Validate answer, if valid replace in grid, if not ask for gridpos again. Returns updated grid (list of lists)
    updated_grid = validate_answer(players[i], grid, player_move)
    # print_grid(updated_grid)

    # check grid for winner
    is_winner = check_for_winner(updated_grid)

    # Turn Over Countdown
    turns -= 1


# NOT USED CODE
# All grid values into empty strings
# a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = " "

# Initialize all grid values into its grid position string
# a1, a2, a3, b1, b2, b3, c1, c2, c3 = 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'

# Values in grid in list of lists
# grid = [[a1, a2, a3],
#         [b1, b2, b3],
#         [c1, c2, c3]]

# Print grid format with grid columns
# print("    1   2   3")
# print(f" A  {a1} | {a2} | {a3}")
# print("   --- --- ---")
# print(f" B  {b1} | {b2} | {b3}")
# print("   --- --- ---")
# print(f" C  {c1} | {c2} | {c3}")
