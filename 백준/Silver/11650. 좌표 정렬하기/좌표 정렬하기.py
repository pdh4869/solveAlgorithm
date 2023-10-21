a = int(input())
d = []
for i in range(a):
    b,c = map(int, input().split())
    d.append([b,c])
    
d.sort(key=lambda x : (x[0], x[1]))

for i in range(a):
    print(d[i][0], d[i][1])