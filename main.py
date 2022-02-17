# FUNCTIONS

# Prints actual grid . Attribute is a list of lists
def print_grid(grid):
    print()
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print("----+----+---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print("----+----+---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")
    print()


# Check whose player's turn is it
def check_turn(turns):
    # Player 1 turn
    if turns % 2 != 0:
        i = 0
    # Player 2 turn
    else:
        i = 1
    print(f"It's {players[i]['name']} turn ('{players[i]['symbol']}').")
    return i


# player is a dict and grid is a list of lists
def ask_and_validate_answer(player, grid):
    while True:
        # Chosen Move Position
        move = input(f"Please {player['name']} choose the grid position where you want to play...\n").upper()

        # Check if Pos Exists
        gridpos_exists = any(move in moves for moves in grid)
        # print(f"Position exists: {gridpos_exists}")

        if gridpos_exists:
            row_index = [i for i, lst in enumerate(grid) if move in lst][0]
            column_index = grid[row_index].index(move)
            grid[row_index][column_index] = player['symbol']
            return grid
        else:
            print("Grid Position doesn't exists or it has already been played in this match.\nPlease enter a valid grid position value.\n")


def check_end_of_game(player, grid, turns_left):
    winner_combinations = [
        grid[0][0] == grid[1][0] == grid[2][0],  # Verticals
        grid[0][1] == grid[1][1] == grid[2][1],
        grid[0][2] == grid[1][2] == grid[2][2],

        grid[0][0] == grid[0][1] == grid[0][2],  # Horizontals
        grid[1][0] == grid[1][1] == grid[1][2],
        grid[2][0] == grid[2][1] == grid[2][2],

        grid[0][0] == grid[1][1] == grid[2][2],  # Diagonals
        grid[2][0] == grid[1][1] == grid[0][2]
       ]

    if winner_combinations[0] or winner_combinations[1] or winner_combinations[2] or winner_combinations[3] or winner_combinations[4] or winner_combinations[5] or winner_combinations[6] or winner_combinations[7]:
        print(f"\n{player['name']} is the Winner!")
        return True
    else:
        if turns_left == 1:
            print("\nIt's a Draw! -.-")
            return True
        print("No winner yet!")
        return False


# MAIN
print("Welcome to My Minimalistic Game of Tic Tac Toe!")

# Players
players = [{"name": "Player 1", "symbol": "X "},
           {"name": "Player 2", "symbol": "O "}]

# Starting Grid Template
grid = [['A1', 'A2', 'A3'],
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3']]

# Control Flow
is_endgame = False
turns = 9
i = 0

# Run game until End of Turns (Draw) or EndGame
while is_endgame is False:
    # Check which player turn is it
    i = check_turn(turns)

    print_grid(grid)

    # Validate answer, if valid replace in grid, if not ask for gridpos again. Returns updated grid (list of lists)
    updated_grid = ask_and_validate_answer(players[i], grid)

    # Check Updated Grid for End of Game
    is_endgame = check_end_of_game(players[i], updated_grid, turns)

    # Turn Over Countdown
    turns -= 1

if is_endgame:
    print_grid(updated_grid)


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
# print(f" A  {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
# print("   --- --- ---")
# print(f" B  {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
# print("   --- --- ---")
# print(f" C  {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")


