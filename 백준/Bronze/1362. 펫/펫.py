i = 0
while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
        
    res = b 
    i += 1
    die = False
    while True:
        pet, weight = map(str, input().split())
        weight = int(weight)

        if pet == '#' and weight == 0:
            break
        
        if not die:
            if pet == 'E':
                res -= weight
            elif pet == 'F':
                res += weight
                
        if res <= 0:
            die = True
         
    if res > a/2 and res < a*2:
        print(i, ":-)")
    elif res <= 0:
        print(i, "RIP")
    else:
        print(i, ":-(")