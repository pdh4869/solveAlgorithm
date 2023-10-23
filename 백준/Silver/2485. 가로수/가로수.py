def gcd(x,y):
    mod = x % y
    while mod != 0:
        x = y
        y = mod
        mod = x % y
    return y
        
n = int(input())
a = int(input())
li = []

for i in range(n-1):
    num = int(input())
    li.append(num-a)
    a = num
    
g = li[0]
for j in range(1,len(li)):
    g = gcd(g,li[j])

res = 0
for k in li:
    res += k//g -1

print(res)