a,b = map(int, input().split())
l = [0] * a

for i in range(b):
    c,d,e = map(int, input().split())
    
    for x in range(c,d+1):
        l[x-1] = e

for j in range(a):
    print(l[j], end=" ")