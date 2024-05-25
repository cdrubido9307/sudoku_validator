import unittest
from sudoku_validator import check_row, check_column, check_subgrid, sudoku

class TestSudokuValidator(unittest.TestCase):
    
    def test_check_row(self):
        for i in range(9):
            self.assertTrue(check_row(i), f"Row {i} failed validation")

    def test_check_column(self):
        for i in range(9):
            self.assertTrue(check_column(i), f"Column {i} failed validation")

    def test_check_subgrid(self):
        subgrid_positions = [(0, 0), (0, 3), (0, 6),
                             (3, 0), (3, 3), (3, 6),
                             (6, 0), (6, 3), (6, 6)]
        for pos in subgrid_positions:
            self.assertTrue(check_subgrid(pos[0], pos[1]), f"Subgrid {pos} failed validation")
    
    def test_invalid_row(self):
        invalid_sudoku = sudoku.copy()
        invalid_sudoku[0][0] = 9  # Introduce an error
        self.assertFalse(check_row(0), "Invalid row passed validation")

    def test_invalid_column(self):
        invalid_sudoku = sudoku.copy()
        invalid_sudoku[0][0] = 9  # Introduce an error
        self.assertFalse(check_column(0), "Invalid column passed validation")
    
    def test_invalid_subgrid(self):
        invalid_sudoku = sudoku.copy()
        invalid_sudoku[0][0] = 9  # Introduce an error
        self.assertFalse(check_subgrid(0, 0), "Invalid subgrid passed validation")

if __name__ == "__main__":
    unittest.main()
