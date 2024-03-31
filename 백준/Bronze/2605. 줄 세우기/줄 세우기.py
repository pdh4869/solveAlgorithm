n = int(input())
l = list(map(int, input().split()))
z = []

for i in range(n):
    z.insert(i-l[i], i+1)
    
for i in range(n):
    print(z[i], end=' ')