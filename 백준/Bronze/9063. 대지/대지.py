a = int(input())
x = []
y = []

for i in range(a):
    b,c = map(int, input().split())
    x.append(b)
    y.append(c)
    
print((max(x)-min(x)) * (max(y)-min(y)))