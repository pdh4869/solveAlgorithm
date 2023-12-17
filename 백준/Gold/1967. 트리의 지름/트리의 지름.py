import sys

sys.setrecursionlimit(10**6)
def dfs(x, weight):
    for i in graph[x]:
        a,b = i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight+b)
    
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
distance = [-1] * (n+1)
distance[1] = 0
dfs(1,0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))