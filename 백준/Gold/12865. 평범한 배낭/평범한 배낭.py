n,k = map(int, input().split())
cache = [[0 for _ in range(k+1)] for _ in range(n+1)]
stuff = [[0,0]]

for i in range(n):
    w,v = map(int, input().split())
    stuff.append([w,v])
    
for i in range(1,n+1):
    for j in range(1,k+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        
        if j < weight:
            cache[i][j] = cache[i-1][j]
        else:
            cache[i][j] = max(value+cache[i-1][j-weight], cache[i-1][j])
            
print(cache[n][k])