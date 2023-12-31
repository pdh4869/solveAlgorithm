import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
max_area = 0

for i in range(n):
    idx = i
    while stack and stack[-1][1] > l[i]:
        idx, height = stack.pop()
        width = (i - idx) * height
        max_area = max(max_area, width)
    stack.append((idx, l[i]))
    
while stack:
    idx, height = stack.pop()
    width = (n - idx) * height
    max_area = max(max_area, width)
print(max_area)