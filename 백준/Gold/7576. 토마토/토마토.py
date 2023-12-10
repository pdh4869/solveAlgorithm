from collections import deque
import sys

m,n  = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
dx = [1,-1,0,0]
dy = [0,0,-1,1]
cnt = 0

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])
            
def bfs():          
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
            
bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt - 1)