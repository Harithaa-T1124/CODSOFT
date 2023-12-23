import tkinter as tk
from tkinter import messagebox
import random


#To check if the board is full
def is_full(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

#To check if there is a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Minimax algorithm with recursion and Alpha-Beta Pruning
def minimax(board, depth, is_maximizing):
    if check_winner(board, human_player):
        return -10 + depth
    elif check_winner(board, ai_player):
        return 10 - depth
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = ai_player
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = ""
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = human_player
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = ""
                    min_eval = min(min_eval, eval)
        return min_eval

#To find the best move for the AI using the Minimax algorithm
def find_best_move(board):
    best_move = None
    best_eval = float("-inf")
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = ai_player
                eval = minimax(board, 0, False)
                board[row][col] = ""
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

#To handle the AI's move
def ai_move():
    if not is_full(board):
        row, col = find_best_move(board)
        board[row][col] = ai_player
        buttons[row][col].config(text=ai_player, state=tk.DISABLED)
        if check_winner(board, ai_player):
            messagebox.showinfo("Result", "AI wins!")
            reset_board()
        elif is_full(board):
            messagebox.showinfo("Result", "It's a draw!")
            reset_board()

#To handle the human player's move
def human_move(row, col):
    if board[row][col] == "" and not is_full(board):
        board[row][col] = human_player
        buttons[row][col].config(text=human_player, state=tk.DISABLED)
        if check_winner(board, human_player):
            messagebox.showinfo("Result", "You win!")
            reset_board()
        else:
            ai_move()
            if is_full(board):
                messagebox.showinfo("Result", "It's a draw!")
                reset_board()

#To reset the board
def reset_board():
    for row in range(3):
        for col in range(3):
            board[row][col] = ""
            buttons[row][col].config(text="", state=tk.NORMAL)

#To create the GUI and start the game
def main():
    global board, buttons, human_player, ai_player

    human_player = "X"
    ai_player = "O"

    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("500x270")

    board = [["" for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(root, text="",font = ("Arial", 10, "bold"), width=20, height=5,command=lambda r=row, c=col: human_move(r, c),fg="white", bg="aqua")
            buttons[row][col].grid(row=row, column=col)

    root.mainloop()

if _name_ == "_main_":
    main()
