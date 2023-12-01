import sys
sys.setrecursionlimit(10**5)
a,b,c = map(int, sys.stdin.readline().split())
dy = (0,1,0,-1)
dx = (1,0,-1,0)
graph = [[0] * b for _ in range(a)]
res = 0
for i in range(c):
    z,x = map(int, sys.stdin.readline().split())
    graph[z-1][x-1] = 1
    
visit = [[False] * b for _ in range(a)]

def dfs(x,y):
    global cnt
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < a and 0 <= ny < b:
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                cnt += 1
                dfs(nx, ny)
                
for i in range(a):
    for j in range(b):
        if graph[i][j] == 1 and not visit[i][j]:
            cnt = 0
            dfs(i, j)
            res = max(res, cnt)
            
print(res)