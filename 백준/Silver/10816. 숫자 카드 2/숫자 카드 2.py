a = int(input())
al = list(map(int, input().split()))
b = int(input())
bl = list(map(int, input().split()))

d = {}

for i in al:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
for i in bl:
    res = d.get(i)
    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')