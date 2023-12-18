from collections import deque
import sys

n = int(sys.stdin.readline())

tree = [[] for _ in range(n+1)]
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    cnt_node = l[0]
    idx = 1
    
    while l[idx] != -1:
        adj_node, adj_cost = l[idx], l[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2
    
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (n+1)
    visited[start] = 0
    res = [0,0]
    
    while q:
        cnt_node, cnt_dist = q.popleft()
        
        for adj_node, adj_dist in tree[cnt_node]:
            if visited[adj_node] == -1:
                cal_dist = cnt_dist + adj_dist 
                q.append((adj_node, cal_dist))
                visited[adj_node] = cal_dist
                
                if res[1] < cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
    return res

point, _ = bfs(1)
print(bfs(point)[1])