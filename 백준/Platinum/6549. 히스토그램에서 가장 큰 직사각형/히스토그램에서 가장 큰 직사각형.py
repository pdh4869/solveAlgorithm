# 히스토그램에서 가장 큰 직사각형
import sys
while True:
    graph = list(map(int, sys.stdin.readline().split()))

    if graph[0] == 0:
        break
    stack = []
    n = graph[0]
    max_area = 0

    for i in range(1, n+1):
        if len(stack) == 0:
            stack.append((i, graph[i]))
        else:
            if stack[-1][1] <= graph[i]:
                stack.append((i, graph[i]))
            else:
                while len(stack) > 0 and stack[-1][1] > graph[i]:
                    remove = stack.pop()
                    if len(stack) == 0:
                        width = i-1
                    else:
                        width = i - stack[-1][0] - 1
                    max_area = max(max_area, remove[1] * width)
                stack.append((i, graph[i]))

    while stack:
        remove = stack.pop()
        if len(stack) == 0:
            width = n
        else:
            width = (n - stack[-1][0])
        max_area = max(max_area, remove[1] * width)
    print(max_area)