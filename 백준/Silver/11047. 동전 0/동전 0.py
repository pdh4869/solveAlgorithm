import sys
n,k = map(int, sys.stdin.readline().split())
l = []

for i in range(n):
    l.append(int(sys.stdin.readline()))
    
l.sort(reverse=True)
cnt = 0
for i in l:
    cnt += (k // i)
    k %= i
print(cnt)