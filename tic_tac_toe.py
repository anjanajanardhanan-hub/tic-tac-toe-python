# Tic Tac Toe Game
# Two Player Game

def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, player):

    if board[0] == player and board[1] == player and board[2] == player:
        return True

    if board[3] == player and board[4] == player and board[5] == player:
        return True

    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # Check columns
    if board[0] == player and board[3] == player and board[6] == player:
        return True

    if board[1] == player and board[4] == player and board[7] == player:
        return True

    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # Check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True

    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


def play_game():

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    player = "X"

    print("\n===== TIC TAC TOE =====")

    while True:

        display_board(board)

        print("Player", player, "'s turn")

        while True:

            choice = input("Enter position (1-9): ").strip()

            if choice == "":
                print("Please enter a position.")
                continue

            try:
                position = int(choice)

            except ValueError:
                print("Please enter a valid number.")
                continue

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")

            elif board[position - 1] == "X" or board[position - 1] == "O":
                print("This position is already occupied.")

            else:
                break

        board[position - 1] = player

        if check_winner(board, player):

            display_board(board)

            print("Player", player, "wins!")
            break

        if "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board:

            display_board(board)

            print("The game is a draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


def main():

    while True:

        play_game()

        answer = input("Do you want to play again? (yes/no): ").strip().lower()

        if answer == "no":
            print("Thank you for playing!")
            break

        elif answer == "yes":
            print("Starting a new game...")

        else:
            print("Invalid choice. Exiting game.")
            break


main()
