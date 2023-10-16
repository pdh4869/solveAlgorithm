a = int(input())
l = [25,10,5,1]

for i in range(a):
    b = int(input())
    for j in l:
        print(b//j, end=' ')
        b = b % j