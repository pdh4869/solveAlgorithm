n = int(input())
now = list(map(int, input().split()))
stack = []
tgt = 1

while now:
    if now[0] == tgt:
        now.pop(0)
        tgt += 1
    else:
        stack.append(now.pop(0))
        
    while stack:
        if stack[-1] == tgt:
            stack.pop()
            tgt += 1
        else:
            break
            
if not stack:
    print("Nice")
else:
    print("Sad")