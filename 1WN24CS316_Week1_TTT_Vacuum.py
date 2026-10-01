import random

# =====================================================================
# 1. TIC-TAC-TOE GAME (WITH USER INPUT)
# =====================================================================

def print_ttt_board(board):
    """Displays the current 3x3 Tic-Tac-Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_ttt_winner(board):
    """Checks horizontal, vertical, and diagonal win paths."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    if " " not in board:
        return "Draw"
    return None

def play_tic_tac_toe():
    print("==========================================")
    print("1. TIC-TAC-TOE GAME (USER VS COMPUTER)")
    print("==========================================")
    print("Board Index Positions (0 to 8):")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 \n")

    board = [" "] * 9

    while True:
        # --- User Turn ('X') ---
        try:
            user_move = int(input("Enter your position (0-8): "))
            if user_move < 0 or user_move > 8 or board[user_move] != " ":
                print("Invalid move! Pick an empty cell between 0 and 8.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")
            continue

        board[user_move] = "X"
        print(f"\nYour Move ('X'):")
        print_ttt_board(board)

        winner = check_ttt_winner(board)
        if winner:
            if winner == "Draw":
                print("Game Result: It's a Draw!\n")
            else:
                print(f"Game Result: Player '{winner}' Wins!\n")
            break

        # --- Computer Turn ('O') ---
        available_moves = [i for i, spot in enumerate(board) if spot == " "]
        comp_move = random.choice(available_moves)
        board[comp_move] = "O"
        print(f"Computer Move ('O') at position {comp_move}:")
        print_ttt_board(board)

        winner = check_ttt_winner(board)
        if winner:
            if winner == "Draw":
                print("Game Result: It's a Draw!\n")
            else:
                print(f"Game Result: Computer ('{winner}') Wins!\n")
            break


# =====================================================================
# 2. VACUUM CLEANER AGENT (AGENT SIMULATION)
# =====================================================================

def run_vacuum_cleaner():
    print("==========================================")
    print("2. VACUUM CLEANER AGENT SIMULATION")
    print("==========================================")
    
    # Getting input status from user
    status_a = input("enter status of room a: ").strip().lower()
    status_b = input("enter status of room b: ").strip().lower()
    location = input("enter current location of agent (a/b): ").strip().lower()
    print()

    rooms = {'a': status_a, 'b': status_b}

    while True:
        print(f"current location : {location}")
        print(f"room a:{rooms['a']} | room b:{rooms['b']}")

        if rooms[location] == 'dirty':
            action = f"suck in room {location}"
            print(f"action:{action}\n")
            rooms[location] = 'clean'
        else:
            other_location = 'b' if location == 'a' else 'a'
            if rooms[other_location] == 'dirty':
                action = f"move to room {other_location}"
                print(f"action:{action}\n")
                location = other_location
            else:
                action = "no operation (both rooms clean)"
                print(f"action:{action}\n")
                break


# =====================================================================
# MAIN EXECUTION
# =====================================================================
if __name__ == "__main__":
    play_tic_tac_toe()
    run_vacuum_cleaner()