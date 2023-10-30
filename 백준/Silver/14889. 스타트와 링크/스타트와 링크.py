inf = 2147000000
res = inf
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited =  [False for _ in range(n)]

def dfs(L,idx):
    global res
    if L == n // 2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += board[i][j]
                elif not visited[i] and not visited[j]:
                    b += board[i][j]
        res = min(res, abs(a-b))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(L+1,i+1)
            visited[i] = False
            

dfs(0,0)
print(res)