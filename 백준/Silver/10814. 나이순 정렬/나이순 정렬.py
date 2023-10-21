a = int(input())
l1 = []


for i in range(a):
    b,c = map(str, input().split())
    b = int(b)
    l1.append([b,c,i])
    
l1.sort(key=lambda x:(x[0],x[2]))

for i in range(a):
    print(l1[i][0],l1[i][1])