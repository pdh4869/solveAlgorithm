n = int(input())

p = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2,1000001):
    if check[i] == 0:
        p.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

for i in range(n):
    cnt = 0
    N = int(input())
    for j in p:
        if j >= N:
            break
        if check[N-j] == 0 and j <= N-j:
            cnt += 1
    print(cnt)