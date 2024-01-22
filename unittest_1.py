import unittest
from tkinter import Tk, Entry
from tkinter.messagebox import showwarning
from unittest.mock import patch  
from Sudoku import SudokuGame  

class TestUserInputValidation(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.game = SudokuGame(self.root, "easy")

    def tearDown(self):
        self.root.destroy()

    def test_validate_entry_valid_input(self):
        row, col = 0, 0
        entry_widget = Entry(self.root)
        entry_widget.insert(0, "5")

        self.game.validate_entry(None, row, col, entry_widget)

        self.assertEqual(self.game.board[row][col], 5)
        # Ensure that no warning message box is shown
        self.assertFalse(showwarning.called)

    def test_validate_entry_invalid_input(self):
        row, col = 0, 0
        entry_widget = Entry(self.root)
        entry_widget.insert(0, "10")

        with patch('tkinter.messagebox.showwarning') as mock_showwarning:
            self.game.validate_entry(None, row, col, entry_widget)

            # Ensure that the internal board remains unchanged
            self.assertEqual(self.game.board[row][col], 0)
            # Ensure that a warning message box is shown for invalid input
            mock_showwarning.assert_called_once_with("Invalid Move", "This number cannot be placed in the selected cell.")

    def test_validate_entry_duplicate_in_row(self):
        row, col = 0, 0
        entry_widget = Entry(self.root)
        entry_widget.insert(0, "5")

        # Set a conflicting value in the same row
        self.game.board[row][col + 1] = 5

        with patch('tkinter.messagebox.showwarning') as mock_showwarning:
            self.game.validate_entry(None, row, col + 1, entry_widget)

            # Ensure that the internal board remains unchanged
            self.assertEqual(self.game.board[row][col + 1], 5)
            # Ensure that a warning message box is shown for an invalid move
            mock_showwarning.assert_called_once_with("Invalid Move", "This number cannot be placed in the selected cell.")

if __name__ == '__main__':
    unittest.main()