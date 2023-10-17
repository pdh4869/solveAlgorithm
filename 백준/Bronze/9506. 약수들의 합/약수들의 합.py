while True:
    a = int(input())
    c = []
    if a == -1:
        break
    
    for i in range(1,a):
        if a % i == 0:
            c.append(i)
                
    if sum(c) == a:
        print(a," = ", " + ".join(str(i) for i in c), sep="")
    else:
        print(a, "is NOT perfect.")