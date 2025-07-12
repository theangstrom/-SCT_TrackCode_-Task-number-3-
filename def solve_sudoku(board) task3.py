def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking"""
    empty = find_empty_cell(board)
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack if solution not found
    
    return False

def find_empty_cell(board):
    """Finds the next empty cell (0) in the board"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    """Checks if a number is valid in a given position"""
    # Check row
    for j in range(9):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    
    return True

def print_board(board):
    """Prints the Sudoku board with borders"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Original Sudoku Puzzle:")
    print_board(puzzle)
    print("\nSolving...\n")
    
    if solve_sudoku(puzzle):
        print("Solved Sudoku:")
        print_board(puzzle)
    else:
        print("No solution exists for this puzzle")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()