def fac(x):
    if x <= 1: return 1
    return x * fac(x-1)

a,b = map(int, input().split())

print(fac(a) // (fac(a-b)*fac(b)))