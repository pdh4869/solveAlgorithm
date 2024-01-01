import sys

def result():
    a = int(sys.stdin.readline())
    l = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [[0] * (a+1) for _ in range(a+1)]
    
    for i in range(1, a+1):
        for j in range(1, a+1):
            if i+1 == j:
                dp[i][j] = l[i] + l[j]
            
    for i in range(a-1, 0, -1):
        for j in range(1, a+1):
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(l[i:j+1])
                
    print(dp[1][a])
    
n = int(sys.stdin.readline())  
for _ in range(n):
    result()