a,b = map(int,input().split())
c = int(input())
d = int(input())

if ((a*d)+b <= (c*d)) and (a <= c):
    print(1)
else:
    print(0)