n = int(input())
b = []
for i in range(n):
    a = int(input())
    b.append(a)
    l = len(b)
    if b[l-1] == 0:
        b.pop()
        b.pop()
print(sum(b))