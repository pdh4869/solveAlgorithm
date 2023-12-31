import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
res = 0

for i in l:
    while stack and stack[-1][0] < i:
        res += stack.pop()[1]
        
    if not stack:
        stack.append((i, 1))
        continue
        
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        res += cnt
        
        if stack:
            res += 1
        stack.append((i, cnt+1))
    else:
        stack.append((i,1))
        res += 1

print(res)