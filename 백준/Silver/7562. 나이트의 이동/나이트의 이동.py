from collections import deque
import sys


dx = [1,-1,-2,2,-2,2,1,-1]
dy = [-2,-2,-1,-1,1,1,2,2]

def bfs(o,p):
    q = deque([[o,p]])
    
    while q:
        x,y = q.popleft()
        
        if x == end_x and y == end_y:
            return graph[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < a and 0 <= ny < a:
                if graph[nx][ny] == 0:
                    q.append([nx,ny])
                    graph[nx][ny] = graph[x][y] + 1
    
n = int(input())

for i in range(n):
    a = int(sys.stdin.readline())
    graph = [[0] * (a) for _ in range(a)]
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())
    print(bfs(start_x, start_y))