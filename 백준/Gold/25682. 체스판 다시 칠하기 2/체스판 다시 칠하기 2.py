import sys
sys.maxsize

def chess(color):
    z = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                val = l[i][j] != color
            else:
                val = l[i][j] == color
            z[i+1][j+1] = z[i][j+1] + z[i+1][j] - z[i][j] + val
    count = sys.maxsize
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            count = min(count, z[i+k-1][j+k-1] - z[i+k-1][j-1] - z[i-1][j+k-1] + z[i-1][j-1])
    return count

n,m,k = map(int, sys.stdin.readline().split())
l = [list(sys.stdin.readline()) for _ in range(n)]
print(min(chess('B'), chess('W')))