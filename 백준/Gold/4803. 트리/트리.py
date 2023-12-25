import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def check(j):
    ret = True
    q = [j]
    while q:
        a = q.pop()
        if visited[a] == 1:
            ret = False
        visited[a] = 1
        for i in dic[a]:
            if i == a:
                ret = False
            
            if visited[i] == 0:
                q.append(i)
                
    return ret

cnt = 0

while True:
    n,m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
        
    ans = 0
    cnt += 1
    dic = defaultdict(list)
    visited = [0] * (n+1)
    for i in range(m):
        a,b = map(int, sys.stdin.readline().split())
        dic[a].append(b)
        dic[b].append(a)
        
    for j in range(1, n+1):
        if visited[j] == 1:
            continue
        
        if check(j):
            ans += 1
            
    if ans > 1:
        print("Case %d: A forest of %d trees."%(cnt,ans))
    elif ans == 1:
        print("Case %d: There is one tree."%cnt)
    else:
        print("Case %d: No trees."%cnt)