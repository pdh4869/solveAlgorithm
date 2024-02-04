n = int(input())

l = {}
for i in range(n):
    a = input()
    if a[0] in l:
        l[a[0]] += 1
    else:
        l[a[0]] = 1
        
res = [] 

for i in l:
    if l[i] >= 5:
        res.append(i)
        
if len(res) > 0:
    res.sort()
    for i in res:
        print(i, end='')
else:
    print('PREDAJA')