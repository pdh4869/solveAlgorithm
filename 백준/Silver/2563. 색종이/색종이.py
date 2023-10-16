a = int(input())
cnt = 0
l1 = [[0 for i in range(101)] for i in range(101)]

for i in range(a):
    b,c = list(map(int, input().split()))
    
    for j in range(b, b+10):
        for k in range(c, c+10):
            l1[j][k] = 1

for i in l1:
    cnt += i.count(1)
print(cnt)