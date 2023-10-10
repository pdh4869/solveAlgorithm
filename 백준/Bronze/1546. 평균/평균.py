N = int(input())
a = list(map(float, input().split()))
c = 0

for i in range(N):
    c += (a[i]/max(a)) * 100
print(c/N)    