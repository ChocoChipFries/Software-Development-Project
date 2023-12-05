import tkinter as tk
from tkinter import messagebox
import random

class Sudoku:
    def __init__(self, parameter, difficulty):
        self.paremeter = parameter
        self.paremeter.title("Sudoku")
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
        if self.difficulty == "easy":
            empty_cells = random.randint(25, 40)
        elif self.difficulty == "medium":
            empty_cells = random.randint(45, 50)
        elif self.difficulty == "hard":
            empty_cells = random.randint(55, 60)
        else:
            raise ValueError("Invalid difficulty level")

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
