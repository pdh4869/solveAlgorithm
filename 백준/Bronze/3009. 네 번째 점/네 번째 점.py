x = []
y = []

res_x = 0
res_y = 0

for i in range(3):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1:
        res_x = x[i]
    
    if y.count(y[i]) == 1:
        res_y = y[i]
    
print(res_x, res_y)