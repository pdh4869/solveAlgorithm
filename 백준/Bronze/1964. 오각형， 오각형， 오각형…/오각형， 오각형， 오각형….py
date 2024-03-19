a = int(input())

res = 5
b = 7
for i in range(a-1):
    res += b
    b += 3
    res %= 45678
    
print(res)