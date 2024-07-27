import numpy as np
import tkinter as tk
from tkinter import messagebox

# Initialize the game board
def initialize_board():
    return np.array([[' ' for _ in range(3)] for _ in range(3)])

# Check for a winner
def check_winner(board, player):
    for row in board:
        if np.all(row == player):
            return True
    for col in board.T:
        if np.all(col == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Check if the board is full
def is_full(board):
    return not np.any(board == ' ')

# Get all valid moves
def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == ' ']

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for move in get_valid_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_valid_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Select the best move for the AI
def best_move(board):
    best_val = -float('inf')
    best_move = None
    for move in get_valid_moves(board):
        board[move] = 'O'
        move_val = minimax(board, 0, False, -float('inf'), float('inf'))
        board[move] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move

# Create the GUI for the game
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = initialize_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.human_turn = True
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('normal', 40), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.board[row, col] == ' ' and self.human_turn:
            self.board[row, col] = 'X'
            self.buttons[row][col].config(text='X')
            if check_winner(self.board, 'X'):
                self.display_winner("Human wins!")
            elif is_full(self.board):
                self.display_winner("It's a draw!")
            else:
                self.human_turn = False
                self.ai_move()

    def ai_move(self):
        move = best_move(self.board)
        self.board[move] = 'O'
        self.buttons[move[0]][move[1]].config(text='O')
        if check_winner(self.board, 'O'):
            self.display_winner("AI wins!")
        elif is_full(self.board):
            self.display_winner("It's a draw!")
        else:
            self.human_turn = True

    def display_winner(self, message):
        response = messagebox.askquestion("Game Over", message + "\nDo you want to play again?")
        if response == 'yes':
            self.reset_board()
        else:
            self.root.quit()

    def reset_board(self):
        self.board = initialize_board()
        self.human_turn = True
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
