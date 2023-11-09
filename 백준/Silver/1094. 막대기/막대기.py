n = int(input())
cnt = 0
x = 64

while n > 0:
    if x > n:
        x = x // 2
    else:
        cnt += 1
        n -= x
        
print(cnt)