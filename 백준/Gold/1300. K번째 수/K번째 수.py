import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 0
end = k

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    
    for i in range(1,n+1):
        tmp += min(mid // i, n)
        
    if tmp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(answer)