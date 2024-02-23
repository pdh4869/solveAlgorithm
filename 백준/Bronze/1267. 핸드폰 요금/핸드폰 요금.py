n = int(input())
l = list(map(int, input().split()))

ys = 0
ms = 0

for i in range(len(l)):
    ys += (l[i] // 30 + 1) * 10
    ms += (l[i] // 60 + 1) * 15
        
if ys == ms:
    print("Y M", ms)
elif ys > ms:
    print("M", ms)
else:
    print("Y", ys)