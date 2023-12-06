from collections import deque
import sys

sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited1[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited1[i] = 1
                
n,m,r = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
visited1 = [0] * (n+1)

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = 1
    
dfs(r)
print()
bfs(r)