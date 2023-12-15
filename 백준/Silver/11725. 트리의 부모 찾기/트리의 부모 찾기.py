import sys

sys.setrecursionlimit(10**6)
def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)
            
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)

for i in range(2, n+1):
    print(visited[i])