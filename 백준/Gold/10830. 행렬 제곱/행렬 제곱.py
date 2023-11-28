import sys

n, b = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
    
def mul(n,a,b):
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j] % 1000
    return res

def square(n, b, a):
    if b == 1:
        return a
    elif b == 2:
        return mul(n,a,a)
    else:
        tmp = square(n, b//2, a)
        if b % 2 == 0:
            return mul(n, tmp, tmp)
        else:
            return mul(n, mul(n, tmp, tmp), a)
        
result = square(n, b, a)
for row in result:
    for col in row:
        print(col % 1000, end=' ')
    print()