a = int(input())

for i in range(a):
    b,c = map(int, input().split())
    org_b = b
    org_c = c
    while c != 0:
        r = b % c
        b = c
        c = r
        
        if c == 0:
            print(org_b*org_c//b)    