import sys
n,k = map(int, input().split())
l = []

for i in range(n):
    l.append(int(input()))
    
l.sort(reverse=True)
cnt = 0
for i in l:
    cnt += (k // i)
    k %= i
print(cnt)