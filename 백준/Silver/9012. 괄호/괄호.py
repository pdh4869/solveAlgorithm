n = int(input())

for i in range(n):
    s = []
    a = input()
    isVPS = True
    
    for j in a:
        if j == '(':
            s.append(j)
        elif j == ')':
            if s:
                s.pop()
            else:
                isVPS = False
                break
            
    if not s and isVPS:
        print("YES")
    elif s or not isVPS:
        print("NO")