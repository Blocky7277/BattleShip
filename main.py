# Set up player boards and variables
player1_board = [[0] * 10 for _ in range(10)]
player2_board = [[0] * 10 for _ in range(10)]
player1_ships = {"A": 5, "B": 4, "C": 3, "D": 3, "E": 2}
player2_ships = {"A": 5, "B": 4, "C": 3, "D": 3, "E": 2}
current_player = 1

def print_board(player_board, player_ships):
    # Print column labels
    print("  " + " ".join(str(i) for i in range(10)))
    # Print rows with row labels and ship characters
    for i, row in enumerate(player_board):
        print(str(i) + " " + " ".join(str(player_ships.get(cell, " ")) for cell in row))

def get_move(player_board):
    # Prompt player for move
    while True:
        move = input("Enter your move (row column): ")
        try:
            row, col = map(int, move.split())
            if player_board[row][col] == 0:
                return row, col
            else:
                print("You have already tried that position!")
        except (ValueError, IndexError):
            print("Invalid input. Enter a valid row and column.")

# Main game loop
while True:
    # Print current player board and remaining ships
    if current_player == 1:
        print("Player 1's turn")
        print_board(player1_board, player1_ships)
        print("Ships remaining:", ", ".join(f"{ship}: {count}" for ship, count in player1_ships.items()))
    else:
        print("Player 2's turn")
        print_board(player2_board, player2_ships)
        print("Ships remaining:", ", ".join(f"{ship}: {count}" for ship, count in player2_ships.items()))

    # Get player move
    row, col = get_move(player1_board if current_player == 1 else player2_board)
    # Update board and check for hit or miss
    if current_player == 1:
        result = player2_board[row][col]
        player1_board[row][col] = result
        if result != 0:
            player2_ships[result] -= 1
            if player2_ships[result] == 0:
                print(f"You sank player 2's {result} ship!")
            else:
                print("You hit player 2's ship!")
        else:
            print("You missed!")
    else:
        result = player1_board[row][col]
        player2_board[row][col] = result
        if result != 0:
            player1_ships[result] -= 1
            if player1_ships[result] == 0:
                print(f"You sank player 1's {result} ship!")
            else:
                print("You hit player 1's ship!")
        else:
            print("You missed!")

    # Check if game is over
    if sum(player1_ships.values()) == 0:
        print("Player 2 wins!")
        break
    elif sum(player2_ships.values()) == 0:
        print("Player 1 wins!")
        break

    # Switch players
    current_player = 1 if current_player == 2 else 2