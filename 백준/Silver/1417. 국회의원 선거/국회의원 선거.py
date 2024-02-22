n = int(input())
ds = int(input())
res = []
cnt = 0 

for i in range(n-1):
    res.append(int(input()))
res.sort(reverse=True)

if n <= 1:
    print(0)
else:
    while res[0] >= ds:
        ds += 1
        res[0] -= 1
        cnt += 1
        res.sort(reverse=True)
    print(cnt)