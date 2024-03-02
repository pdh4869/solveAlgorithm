n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    
cnt1 = 0
cnt2 = 0
l_max = 0
r_max = 0

for i in l:
    if i > l_max:
        l_max = i
        cnt1 += 1
    
for i in l[::-1]:
    if i > r_max:
        r_max = i
        cnt2 += 1
        
print(cnt1)
print(cnt2)