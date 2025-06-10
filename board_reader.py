# board_reader.py
import chess

def update_board_and_fen(board_2d, turn):
    fen_rows = []
    for row in board_2d:
        empty = 0
        fen_row = ""
        for cell in row:
            if cell == "x":
                empty += 1
            else:
                if empty > 0:
                    fen_row += str(empty)
                    empty = 0
                fen_row += cell
        if empty > 0:
            fen_row += str(empty)
        fen_rows.append(fen_row)

    fen_board = "/".join(fen_rows)
    return f"{fen_board} {turn} - - 0 1"
