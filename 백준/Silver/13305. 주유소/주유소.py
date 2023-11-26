# 주유소
n = int(input())
l = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt = 0
m = c[0]

for i in range(n-1):
    if c[i] < m:
        m = c[i]
    cnt += m*l[i]
    
print(cnt)