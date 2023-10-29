def recur(num):
    if num == m:
        print(' '.join(map(str, res)))
        return 
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            res.append(i+1)
            recur(num+1)
            
            visited[i] = False
            res.pop()
    
n,m = map(int, input().split())
res = []
visited = [False] * n

recur(0)