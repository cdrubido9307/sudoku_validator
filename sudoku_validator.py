import threading

# Example Sudoku puzzle (a solved one)
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

# Function to check if a row is valid
def check_row(row):
    return sorted(sudoku[row]) == list(range(1, 10))

# Function to check if a column is valid
def check_column(col):
    column = [sudoku[row][col] for row in range(9)]
    return sorted(column) == list(range(1, 10))

# Function to check if a 3x3 subgrid is valid
def check_subgrid(start_row, start_col):
    subgrid = [sudoku[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]
    return sorted(subgrid) == list(range(1, 10))

def main():
    threads = []
    results = []

    # Creating threads to check rows
    for i in range(9):
        t = threading.Thread(target=lambda r=i: results.append(check_row(r)))
        threads.append(t)
        t.start()
    
    # Creating threads to check columns
    for i in range(9):
        t = threading.Thread(target=lambda c=i: results.append(check_column(c)))
        threads.append(t)
        t.start()
    
    # Creating threads to check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            t = threading.Thread(target=lambda r=i, c=j: results.append(check_subgrid(r, c)))
            threads.append(t)
            t.start()
    
    # Waiting for threads to complete
    for t in threads:
        t.join()

    if all(results):
        print("All checks passed.")
    else:
        print("Some checks failed.")

if __name__ == "__main__":
    main()
