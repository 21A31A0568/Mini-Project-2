b = [
    [0, 5, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 3, 0, 0, 0, 2, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 6, 0],
    [0, 0, 5, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 0, 0, 0, 0, 1, 0, 0]
]

def find(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
    return None  # No empty space left

def isvalid(b, r, col, no):
    for i in range(len(b[0])):
        if b[r][i] == no:  # Check row
            return False
    for i in range(len(b)):
        if b[i][col] == no:  # Check column
            return False
    strow = 3 * (r // 3)
    stcol = 3 * (col // 3)
    for i in range(strow, strow + 3):
        for j in range(stcol, stcol + 3):
            if b[i][j] == no:  # Check 3x3 subgrid
                return False
    return True

def play(b):
    empty = find(b)
    if empty is None:
        return True  # Sudoku solved
    
    i, j = empty
    for no in range(1, 10):
        if isvalid(b, i, j, no):
            b[i][j] = no
            if play(b):  # If the board is solved, return True
                return True
            b[i][j] = 0  # Backtrack if no valid solution

    return False  # No valid number found

if play(b):
    for row in b:
        print(row)
else:
    print("No valid solution exists")
