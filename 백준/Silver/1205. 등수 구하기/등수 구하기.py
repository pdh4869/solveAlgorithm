n,k,p = map(int, input().split())
cnt = 0

if n == 0:
    print(1)
else:
    l = list(map(int, input().split()))
    if n == p and l[-1] >= k:
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if l[i] <= k:
                res = i+1
                break
        print(res)