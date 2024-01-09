import sys

n,m = map(int, sys.stdin.readline().split())
l1 = [0] * m
l2 = [0] * m

for i in range(m):
    l1[i], l2[i] = map(int, sys.stdin.readline().split())

min1 = min(l1)
min2 = min(l2)

if min1 > min2 * 6:
    print(n*min2)
else:
    if (n % 6) * min2 < min1:
        print(((n // 6) * min1) + ((n % 6) * min2))
    else:
        print(((n // 6) + 1) * min1)