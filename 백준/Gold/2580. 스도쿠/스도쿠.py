def chk_row(x,n):
    for i in range(9):
        if res[x][i] == n:
            return False
    return True

def chk_col(y,n):
    for i in range(9):
        if res[i][y] == n:
            return False
    return True

def square(y,x,n):
    for i in range(3):
        for j in range(3):
            if res[(y//3)*3 + i][(x//3)*3 + j] == n:
                return False
    return True

def sudoku(n):
    if n == len(blank):
        for i in res:
            print(*i)
        exit()
        
    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        
        if chk_col(x,i) and chk_row(y,i) and square(y,x,i):
            res[y][x] = i
            sudoku(n+1)
            res[y][x] = 0
    
import sys

blank = []
res = []
for i in range(9):
    board = list(map(int, sys.stdin.readline().rstrip().split()))
    res.append(board)

for i in range(9):
    for j in range(9):
        if res[i][j] == 0:
            blank.append([i,j])
            
sudoku(0)