n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
res = 0

for i in range(n):
    res += (a[i] * max(b))
    b.remove(max(b))
        
print(res)