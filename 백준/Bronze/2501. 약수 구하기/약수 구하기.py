a,b = map(int, input().split())
c = []
cnt = 0

for i in range(1,a+1):
    if a % i == 0:
        c.append(i)
        
if b-1 < len(c):
    print(c[b-1])
else:
    print(0)