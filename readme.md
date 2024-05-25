# Sudoku Validator

## Project Overview
This project implements a multithreaded application to validate a 9x9 Sudoku puzzle solution. The Sudoku grid must satisfy the following conditions:
- Each row contains the digits 1 through 9 exactly once.
- Each column contains the digits 1 through 9 exactly once.
- Each of the nine 3x3 subgrids contains the digits 1 through 9 exactly once.

The implementation uses Python threading to concurrently check these conditions for rows, columns, and subgrids.

## Files Included
- `sudoku_validator.py`: Contains the main implementation of the Sudoku validator.
- `test_sudoku_validator.py`: Contains unit test cases for the Sudoku validator.
- `README.md`: This file, explaining the project and how to run the code and tests.

## Implementation Details
### `sudoku_validator.py`
- **check_row(row)**: Validates if a specific row contains all digits from 1 to 9.
- **check_column(col)**: Validates if a specific column contains all digits from 1 to 9.
- **check_subgrid(start_row, start_col)**: Validates if a 3x3 subgrid starting at `(start_row, start_col)` contains all digits from 1 to 9.
- **main()**: Orchestrates the creation and management of threads to validate the Sudoku grid concurrently.

### `test_sudoku_validator.py`
- Contains unit tests to verify the functionality of row, column, and subgrid validation.
- Tests include both valid and invalid cases to ensure robustness.

## How to Run the Code
1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Run the Sudoku Validator**:
    ```bash
    python sudoku_validator.py
    ```
    This will execute the `main()` function in `sudoku_validator.py`, which creates multiple threads to validate the Sudoku grid concurrently.

## How to Run Unit Tests
1. **Ensure you are in the project directory**:
    ```bash
    cd <repository_directory>
    ```

2. **Run the Unit Tests**:
    ```bash
    python -m unittest test_sudoku_validator.py
    ```
    This will execute all the unit tests defined in `test_sudoku_validator.py` and print the results.

## Example Output
When you run `sudoku_validator.py`, the output will indicate whether each row, column, and subgrid is valid. For example following valid sudoku:

```python
sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
```


- Row 0 is valid.
- Row 1 is valid.

- Column 0 is valid.
- Column 1 is valid.

- Subgrid starting at (0, 0) is valid.
- Subgrid starting at (0, 3) is valid.

- All checks completed.

By opening the `sudoku_validator.py` file and replacing the sudoku matrix by any desire matrix you can use the program with any desire custom sudoku matrix.

## Execute via Replit
For easy execution without having to run locally bellow I provided a Replit environment that will allow you to run the project with a simple click. Check instructions Bellow:

- Open the URL: https://replit.com/@cdrubido/sudokuvalidator?v=1
- On the right hand side click click the Fork green button and fork the project.
- Once the project is Forked you can open the `sudoku_validator.py` file. 
- Finally Click RUN.
- To run the unittest open the terminal in the Replit environment and run the command to execute the unittest provided above.
