import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

stack = []
b_len = len(b)

for i in range(len(a)):
    stack.append(a[i])
    if ''.join(stack[-b_len:]) == b:
        for _ in range(b_len):
            stack.pop()
        
if stack:
    print(''.join(stack))
else:
    print("FRULA")