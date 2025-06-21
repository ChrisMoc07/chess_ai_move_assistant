# Chess AI Move Assistant ♟️🤖

> A real-time chess analysis tool that combines AI and Stockfish to instantly suggest the best move from a physical board snapshot.

---

## 🧠 Overview

**Chess AI Move Assistant** is a Python-based application that reconstructs a real chessboard state from user input and analyzes the best possible move using the Stockfish chess engine. Designed to dramatically reduce the manual effort of traditional notation entry, this tool helps players review positions and improve strategic thinking on the fly.

Built to serve competitive and casual players in the Chicagoland Chess community — and beyond.

---

## 💡 Key Features

- 🧩 **AI-Powered Move Suggestions**  
  Automatically fetches the best move for any position using Stockfish 17.

- 📷 **Real-Board State Simulation** *(Coming Soon)*  
  Add-on module will allow image recognition input via camera to detect board state.

- 🧾 **FEN Generation**  
  Converts board input into FEN (Forsyth-Edwards Notation) format in real-time.

- 🔁 **Interactive Terminal Interface**  
  Lightweight and clean — no GUI needed (yet).

---

## 🔧 Tech Stack

- **Python 3.11**
- **Stockfish 17.1**
- `python-chess`
- `pygame` *(optional/future UI)*
- Custom FEN generation module

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/ChrisMoc07/chess_ai_move_assistant.git
cd chess_ai_move_assistant
2. Setup Virtual Environment (Python 3.11 Required)
bash
Copy
Edit
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
