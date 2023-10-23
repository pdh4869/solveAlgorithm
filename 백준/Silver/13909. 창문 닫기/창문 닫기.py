n = int(input())
res = 0
x = 1
while x*x <= n:
    x += 1
    res += 1
print(res)