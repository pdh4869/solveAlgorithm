a,b = map(int, input().split())
l = [i for i in range(1,a+1)]
i = 0

print('<', end='')
while len(l) != 0:
    i = (i+b-1) % len(l)
    if len(l) == 1:
        print(l.pop(i), end='')
    else:
        print(l.pop(i), end=', ')
print('>')