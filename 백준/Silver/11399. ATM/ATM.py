n = int(input())
l = list(map(int, input().split()))
l.sort()
cnt = 0
for i in range(1,n+1):
    cnt += sum(l[0:i])
    
print(cnt)