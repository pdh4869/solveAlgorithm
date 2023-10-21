a,b = map(int, input().split())
c = list(map(int, input().split()))
c.sort(reverse=True)
d = []

for i in range(b):
    d.append(c[i])
    
print(min(d))