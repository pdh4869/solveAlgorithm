import sys

k,n = map(int, sys.stdin.readline().split())
z = []
for i in range(k):
    z.append(int(sys.stdin.readline()))
    
start = 1
end = max(z)

while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in z:
        line += i // mid
        
    if line >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)