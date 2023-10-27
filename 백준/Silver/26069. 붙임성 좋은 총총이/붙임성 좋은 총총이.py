n = int(input())
a = set()
a.add("ChongChong")
for i in range(n):
    b,c = input().split()
    
    if b == 'ChongChong' or c == 'ChongChong':
        a.add(b), a.add(c)

    if b in a or c in a:
        a.add(b), a.add(c)

print(len(a))