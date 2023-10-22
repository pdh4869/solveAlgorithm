a,b = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
d1 = {}
d2 = {}

for i in al:
    d1[i] = 1

for i in bl:
    d2[i] = 1
    
print(len(d1.keys() - d2.keys()) + len(d2.keys() - d1.keys()))