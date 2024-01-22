import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, master, difficulty):
        self.master = master
        self.master.title("Sudoku Game")
        self.difficulty = difficulty
        self.board = self.generate_board()
        self.initial_board = [row[:] for row in self.board]
        self.create_widgets()

    def generate_board(self):
        board = [[0] * 9 for _ in range(9)]
        self.solve_sudoku(board)
        self.remove_numbers(board)
        return board

    def solve_sudoku(self, board):
        empty_cell = self.find_empty_cell(board)
        
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in random.sample(range(1, 10), 9):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num

                if self.solve_sudoku(board):
                    return True

                board[row][col] = 0

        return False

    def remove_numbers(self, board):
        difficulty_levels = {
            "easy": (36, 40),
            "medium": (46, 50),
            "hard": (56, 60)
        }

        empty_cells = random.randint(*difficulty_levels[self.difficulty])

        for _ in range(empty_cells):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while board[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            board[row][col] = 0

    def is_valid_move(self, board, row, col, num):
        if num in board[row] or num in [board[i][col] for i in range(9)]:
            return False

        subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=450, height=450)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        for i in range(1, 10):
            for j in range(1, 10):
                x, y = (j - 1) * 50, (i - 1) * 50
                cell_value = self.board[i - 1][j - 1]
                if cell_value != 0:
                    self.canvas.create_text(x + 25, y + 25, text=str(cell_value), font=('Helvetica', 16, 'bold'), tags='numbers')
                else:
                    entry = tk.Entry(self.master, width=2, font=('Helvetica', 16), justify='center')
                    entry.bind('<KeyRelease>', lambda event, row=i-1, col=j-1, widget=entry: self.validate_entry(event, row, col, widget))
                    entry.grid(row=i, column=j)

        solve_button = tk.Button(self.master, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=10, column=0, columnspan=5, pady=10)

        reset_button = tk.Button(self.master, text="Reset", command=self.reset_puzzle)
        reset_button.grid(row=10, column=5, columnspan=5, pady=10)

    def validate_entry(self, event, row, col, widget):
        value = widget.get()
        if value.isdigit() and 1 <= int(value) <= 9:
            if self.is_valid_move(self.board, row, col, int(value)):
                self.board[row][col] = int(value)
            else:
                messagebox.showwarning("Invalid Move", "This number cannot be placed in the selected cell.")
                widget.delete(0, tk.END)
                widget.insert(0, "")
        else:
            widget.delete(0, tk.END)

    def solve_puzzle(self):
        for i in range(1, 10):
            for j in range(1, 10):
                widget = self.master.nametowidget(f'!entry{i}.{j}')
                if widget.get() == "":
                    widget.insert(0, str(self.initial_board[i - 1][j - 1]))

    def reset_puzzle(self):
        for i in range(1, 10):
            for j in range(1, 10):
                widget = self.master.nametowidget(f'!entry{i}.{j}')
                widget.delete(0, tk.END)
                widget.insert(0, "")
                self.board[i - 1][j - 1] = 0

def start_game(difficulty):
    root = tk.Tk()
    game = SudokuGame(root, difficulty)
    root.mainloop()

def difficulty_selected(difficulty_var):
    difficulty = difficulty_var.get()
    start_game(difficulty)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sudoku Difficulty Selection")

    difficulty_label = tk.Label(root, text="Select Difficulty:")
    difficulty_label.pack(pady=10)

    difficulty_var = tk.StringVar()
    difficulty_var.set("easy")

    easy_button = tk.Radiobutton(root, text="Easy", variable=difficulty_var, value="easy")
    easy_button.pack()

    medium_button = tk.Radiobutton(root, text="Medium", variable=difficulty_var, value="medium")
    medium_button.pack()

    hard_button = tk.Radiobutton(root, text="Hard", variable=difficulty_var, value="hard")
    hard_button.pack()

    start_button = tk.Button(root, text="Start Game", command=lambda: difficulty_selected(difficulty_var))
    start_button.pack(pady=20)

    root.mainloop()
