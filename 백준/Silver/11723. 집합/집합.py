import sys

n = int(sys.stdin.readline())
s = []

for i in range(n):
    a = list(sys.stdin.readline().split())
    if len(a) == 2:
        a[1] = int(a[1])
    
    if a[0] == 'add':
        if a[1] not in s:
            s.append(a[1])
    elif a[0] == 'remove':
        if a[1] in s:
            s.pop(s.index(a[1]))
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if a[1] in s:
            s.pop(s.index(a[1]))
        else:
            s.append(a[1])
    elif a[0] == 'all':
        s = [i for i in range(1,21)]
    elif a[0] == 'empty':
        s = []
