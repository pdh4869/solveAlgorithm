M = int(input())
N = int(input())

cnt2 = 0
res = []

for i in range(M, N+1):
    cnt1 = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                cnt1 += 1
                break
                
        if cnt1 == 0:
            res.append(i)
                

if len(res) > 0:
    print(sum(res))
    print(min(res))
else:
    print(-1)