n = int(input())
l = list(map(int, input().split()))

res = 0
s = []
for i in range(n):
    if l[i] in s:
        res += 1
    else:
        s.append(l[i])
        
print(res)