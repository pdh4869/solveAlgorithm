l = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
for i in range(1, len(l)):
    if l[i-1] > l[i]:
        cnt1 += 1
    else:
        cnt2 += 1
        
if cnt2 == 7:
    print('ascending')
elif cnt1 == 7:
    print('descending')
else:
    print('mixed')