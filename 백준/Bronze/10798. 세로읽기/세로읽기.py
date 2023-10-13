a = []
leng = []
for i in range(5):
    b = input()
    a.append(b)
    leng.append(len(b))
    
for j in range(max(leng)):
    for i in range(5):
        if j < leng[i]:
            print(a[i][j], end='')