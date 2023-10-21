import sys

a = int(sys.stdin.readline())
b = []
for i in range(a):
    b.append(int(sys.stdin.readline()))
b.sort()
for i in range(a):
    print(b[i])