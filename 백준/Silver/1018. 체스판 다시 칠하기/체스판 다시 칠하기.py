n,m = map(int, input().split())
c = []
res = []
for i in range(n):
    c.append(input())
    

for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if c[a][b] != 'B':
                        cnt1 += 1
                    if c[a][b] != 'W':
                        cnt2 += 1
                else:
                    if c[a][b] != 'W':
                        cnt1 += 1
                    if c[a][b] != 'B':
                        cnt2 += 1
                
        res.append(cnt1)
        res.append(cnt2)

print(min(res))