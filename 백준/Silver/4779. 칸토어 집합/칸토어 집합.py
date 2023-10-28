def cantor(list):
    if len(list) <= 1:
        return list
    
    branch = len(list) // 3
    first = cantor(list[:branch])
    second = ' ' * branch
    third = cantor(list[branch * 2:])
    
    return first + second + third

while True:
    try:
        b = int(input())
        c = '-' * (3**b)

        l = cantor(c)
        print("".join(l))
    except EOFError:
        break