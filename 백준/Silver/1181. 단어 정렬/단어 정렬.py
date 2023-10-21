a = int(input())
b = []

for i in range(a):
    b.append(input())

b = list(set(b))
b.sort()
b.sort(key=lambda x:len(x))


for i in b:
    print(i)