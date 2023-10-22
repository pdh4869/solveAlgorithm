a = input()
b = []

for i in range(len(a)):
    b.append(a[i])
    
for i in range(len(a)):
    for j in range(i,len(a)):
        b.append(a[i:j+1])
print(len(set(b)))