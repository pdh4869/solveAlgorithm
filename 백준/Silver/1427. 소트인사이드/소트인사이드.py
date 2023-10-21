a = int(input())
b = []
while a > 0:
    b.append(a % 10)
    a //= 10
    
b.sort(reverse=True)

for i in b:
    print(i,end="")