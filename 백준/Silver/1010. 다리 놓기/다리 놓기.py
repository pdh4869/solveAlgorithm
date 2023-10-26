def fac(x):
    if x <= 1: return 1
    return x * fac(x-1)

n = int(input())
for i in range(n):
    b,a = map(int, input().split())
    print(fac(a) // (fac(a-b)*fac(b)))