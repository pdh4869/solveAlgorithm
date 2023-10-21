import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
c = sorted(list(set(b)))

dic = {c[i] : i for i in range(len(c))}
for i in b:
    print(dic[i], end=' ')