def recur(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return 
    
    for i in range(start,n+1):
        if i not in res:
            res.append(i)
            recur(i+1)
            res.pop()
    
n,m = map(int, input().split())
res = []

recur(1)