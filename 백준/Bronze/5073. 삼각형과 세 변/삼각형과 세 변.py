while True:
    a = list(map(int, input().split()))
    b = list(a)
    
    max1 = max(a)
    a.remove(max1)
    sum1 = sum(a)
    
    if b[0]!=0 and b[1]!=0 and b[2]!=0:
        if max1 < sum1:
            if b[0]==b[1]==b[2]:
                print("Equilateral")
            elif b[0]==b[1] or b[1]==b[2] or b[2]==b[0]:
                print("Isosceles")
            elif b[0]!=b[1]!=b[2]:
                print("Scalene")
        else:
            print("Invalid")
    else:
        break