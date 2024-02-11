n,l,d = map(int, input().split())

l += 5
res = 0
time = d
for i in range(n):
    res += l
    while True:
        if time < res-5: 
            time += d
        else:
            break
    
    if res-5 <= time < res: 
        break
print(time)