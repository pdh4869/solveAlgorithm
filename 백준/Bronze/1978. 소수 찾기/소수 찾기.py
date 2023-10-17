a = int(input())
cnt2 = 0

b = list(map(int, input().split()))
    
for i in b:
    cnt1 = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                cnt1 += 1
        
        if cnt1 == 0:
            cnt2 += 1
            
print(cnt2)