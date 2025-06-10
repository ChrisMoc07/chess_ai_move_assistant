# main.py

from board_reader import update_board_and_fen
from stockfish_engine import get_best_move

# ANSI escape codes for color
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def color_piece(piece):
    if piece == 'x':
        return piece  # leave x uncolored
    if piece.isupper():  # White
        return CYAN + piece + RESET
    elif piece.islower():  # Black
        return RED + piece + RESET
    return piece

def print_board(board):
    print("\n  a b c d e f g h")
    for i in range(8):
        row = board[i]
        print(f"{8 - i} ", end="")
        for cell in row:
            print(color_piece(cell), end=" ")
        print(f"{8 - i}")
    print("  a b c d e f g h\n")

def main():
    # Init empty board
    board = [
        list("rnbqkbnr"),
        list("pppppppp"),
        list("xxxxxxxx"),
        list("xxxxxxxx"),
        list("xxxxxxxx"),
        list("xxxxxxxx"),
        list("PPPPPPPP"),
        list("RNBQKBNR")
    ]

    side_input = input("Do you want to play as white (w) or black (b)? ").strip().lower()
    if side_input == 'b':
        print("[INFO] You are playing: Black to White (BtoW)")
        turn = 'b'
    else:
        print("[INFO] You are playing: White to Black (WtoB)")
        turn = 'w'

    while True:
        print("\nYour board:")
        print_board(board)

        fen = update_board_and_fen(board, turn)
        print(f"FEN: {fen}")

        try:
            best_move = get_best_move(fen)
            print(f"BEST MOVE: {best_move}")
        except Exception as e:
            print(f"[ERROR] {e}")

        move = input("Enter your move (e.g., e2e4) or 'q' to quit: ").strip().lower()
        if move == 'q':
            break

        try:
            from_square = move[:2]
            to_square = move[2:]

            row_from = 8 - int(from_square[1])
            col_from = ord(from_square[0]) - ord('a')
            row_to = 8 - int(to_square[1])
            col_to = ord(to_square[0]) - ord('a')

            piece = board[row_from][col_from]
            board[row_from][col_from] = 'x'
            board[row_to][col_to] = piece

            turn = 'b' if turn == 'w' else 'w'

        except Exception as err:
            print(f"Invalid move format. Try again. ({err})")

if __name__ == "__main__":
    main()