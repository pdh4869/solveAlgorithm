n = int(input())

for i in range(n):
    a = input()
    b = a[::-1]
    c = int(a) + int(b)
    c = str(c)
    
    if c == c[::-1]:
        print('YES')
    else:
        print('NO')