# 주유소
n = int(input())
l = list(map(int, input().split()))
c = list(map(int, input().split()))
z = []
tmp = sum(l) - l[0]
cnt = (l[0] * c[0])

for i in range(1,n-1):
    z.append(tmp * c[i])
    
print(min(z) + cnt)