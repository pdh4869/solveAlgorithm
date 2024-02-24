n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = 0
for i in b:
    while True:
        if i <= a[idx]:
            a[idx] -= i
            break
        
        idx += 1
print(sum(a))