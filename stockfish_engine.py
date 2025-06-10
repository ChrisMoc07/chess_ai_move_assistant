# stockfish_engine.py

import chess
import chess.engine

def get_best_move(fen, stockfish_path="stockfish/stockfish-windows-x86-64-avx2.exe", time_limit=0.1):
    board = chess.Board(fen)
    try:
        engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    except FileNotFoundError:
        raise Exception(f"Could not find Stockfish engine at {stockfish_path}")
    
    result = engine.play(board, chess.engine.Limit(time=time_limit))
    engine.quit()

    return str(result.move)
