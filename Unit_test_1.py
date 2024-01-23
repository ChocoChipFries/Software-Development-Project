import unittest
from tkinter import Tk, StringVar, Entry, Canvas
from tkinter import messagebox
from Sudoku_another import SudokuGame
from Sudoku_another import SudokuEntry


class TestSudokuGame(unittest.TestCase):

    def setUp(self):
        self.root = Tk()

    def test_generate_board(self):
        game = SudokuGame(self.root, "easy")
        board = game.generate_board()

        # Check if the generated board is a 9x9 grid
        self.assertEqual(len(board), 9)
        for row in board:
            self.assertEqual(len(row), 9)

        # Check if the generated board is solvable
        solved_board = [row[:] for row in board]
        self.assertTrue(game.solve_sudoku(solved_board))

    def test_is_valid_move(self):
        game = SudokuGame(self.root, "easy")
        board = game.generate_board()

        print("Initial Board:")
        for row in board:
            print(row)
        valid_move = game.is_valid_move(board, 0, 0 ,1)
        print(f"Valid Move:{valid_move}")
        
        print("Board after Valid Move:")
        for row in board:
            print(row)
        
        invalid_move = game.is_valid_move(board, 0, 1, 1)
        print(f"Invalid Move: {invalid_move}")

        print("Board after Invalid Move:")
        for row in board:
            print(row)

    def test_find_empty_cell(self):
        game = SudokuGame(self.root, "easy")
        board = game.generate_board()

        # Test finding an empty cell in an empty board
        empty_board = [[0] * 9 for _ in range(9)]
        self.assertEqual(game.find_empty_cell(empty_board), (0, 0))

if __name__ == '__main__':
    unittest.main()
