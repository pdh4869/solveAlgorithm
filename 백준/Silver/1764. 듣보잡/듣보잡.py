a,b = map(int, input().split())
ad = {}
cnt = 0

for i in range(a):
    c = input()
    ad[c] = 0
    

for i in range(b):
    d = input()
    if d in ad.keys():
        ad[d] += 1
        cnt += 1
        
ad2 = dict(sorted(ad.items()))

print(cnt)
for i in ad2:
    if ad2[i] != 0:
        cnt += 1
        print(i)