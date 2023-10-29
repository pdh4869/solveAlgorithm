import sys

def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def nqueen(x):
    global res
    if x == n:
        res += 1
        return

    for i in range(n):
        if chk[i]:
            continue
            
        row[x] = i
        if check(x):
            chk[i] = True
            nqueen(x+1)
            chk[i] = False
      
    
n = int(sys.stdin.readline())
res = 0
row = [0] * n
chk = [False] * n

nqueen(0)
print(res)