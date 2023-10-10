l = []
for i in range(9):
    a = int(input())
    l.append(a)
print(max(l))
print(l.index(max(l))+1)