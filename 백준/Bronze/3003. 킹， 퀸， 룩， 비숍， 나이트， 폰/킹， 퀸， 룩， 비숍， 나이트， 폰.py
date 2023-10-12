a = list(map(int, input().split(' ')))

c = [1,1,2,2,2,8]
d = [0,0,0,0,0,0]
for i in range(len(c)):
    d[i] = c[i] - a[i]
    print(d[i], end=' ')