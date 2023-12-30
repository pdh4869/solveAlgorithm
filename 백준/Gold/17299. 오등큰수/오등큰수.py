from collections import Counter
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dic = Counter(a)
res = [-1] * n
stack = [0]

for i in range(1,n):
    while stack and dic[a[stack[-1]]] < dic[a[i]]:
        res[stack.pop()] = a[i]
    stack.append(i)
    
print(*res)