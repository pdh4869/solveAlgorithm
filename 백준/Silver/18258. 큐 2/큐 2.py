from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    b = list(sys.stdin.readline().split())
    
    if b[0] == 'push':
        queue.append(b[1])
    elif b[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif b[0] == 'size':
        print(len(queue))
    elif b[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif b[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif b[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)