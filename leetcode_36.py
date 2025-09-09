#box = [[5,3,"."],
#       [6,".","."],
#       [".",9,8]]
#box = [[1,".","."],
#       [".",1,"."],
#      [".",".",1]]

grid = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
def validate_row(grid):
    for i in range(len(grid)):
        myset = set()
        for j in range(len(grid[i])):
            if grid[i][j] in myset:
                return False
            elif grid[i][j]!=".":
                myset.add(grid[i][j])
        return True
    
def validate_column(grid):
    for i in range(len(grid)):
        myset = set()
        for j in range(len(grid[i])):
            if grid[j][i] in myset:
                return False
            elif grid[j][i]!=".":
                myset.add(grid[j][i])
        return True
    
def validate_box(box,x,y):
    myset = set()
    for i in range(x,x+3):
        for j in range(y,y+3):
            if box[i][j] in myset:
                return False
            elif box[i][j]!=".":
                myset.add(box[i][j])
    return True
'''
def validate_grid(grid):
    x = 0
    y = 0
    while y<9:
        valid = validate_box(grid,x,y)
        if valid:
            if x+3<9:
                x+=3
            else:
                x = 0
                y +=3
        else:
            return False
    return True
'''
def validate_grid(grid):
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if not validate_box(grid, x, y):
                return False
    return True

def validate_sudoku(grid):
    if validate_row(grid) and validate_column(grid) and validate_grid(grid):
        return True
    else:
        return False
    
print(validate_sudoku(grid))
