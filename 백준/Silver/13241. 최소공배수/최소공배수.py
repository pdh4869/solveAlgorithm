a,b = map(int, input().split())
org_a, org_b = a,b
while b != 0:
    r = a % b
    a = b
    b = r
    
    if b == 0:
        print(org_a*org_b//a)