from collections import deque
import sys

n = int(sys.stdin.readline())
d = deque([])

for i in range(n):
    b = list(map(int, sys.stdin.readline().split()))
    if b[0] == 1:
        d.appendleft(b[1])
    elif b[0] == 2:
        d.append(b[1])
    elif b[0] == 3:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif b[0] == 4:
        if d:
            print(d.pop())
        else:
            print(-1)
    elif b[0] == 5:
        print(len(d))
    elif b[0] == 6:
        if d:
            print(0)
        else:
            print(1)
    elif b[0] == 7:
        if d:
            print(d[0])
        else:
            print(-1)
    elif b[0] == 8:
        if d:
            print(d[-1])
        else:
            print(-1)