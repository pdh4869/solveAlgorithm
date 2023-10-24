import sys

a = int(sys.stdin.readline())
stack = []

for i in range(a):
    d = list(map(int, sys.stdin.readline().split()))
    
    if d[0] == 1:
        stack.append(d[1])
    elif d[0] == 2:
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif d[0] == 3:
        print(len(stack))
    elif d[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif d[0] == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1) 