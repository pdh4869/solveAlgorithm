import sys
n,m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(h)

while start <= end:
    mid = (start + end) // 2
    l = 0
    
    for i in h:
        if i >= mid:
            l += i - mid
        
    if l >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)