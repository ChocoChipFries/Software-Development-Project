import unittest
from tkinter import Tk
from Sudoku_another import SudokuGame, SudokuEntry

class TestSudokuGame(unittest.TestCase):

    def setUp(self):
        self.root = Tk()

    def test_solve_and_reset_puzzle(self):
        game = SudokuGame(self.root, "easy")

        # Store the initial state of the board
        initial_board = [row[:] for row in game.board]

    def solve_puzzle(self):
        for i in range(9):
            for j in range(9):
                widget_name = f'!entry{i + 1}.{j + 1}'  # Use the correct widget name
                widget = self.master.nametowidget(widget_name)
                if widget.get() == "":
                    widget.insert(0, str(self.initial_board[i][j]))
                    
    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()

