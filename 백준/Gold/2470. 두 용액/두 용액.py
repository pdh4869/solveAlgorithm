import math
import sys

n = int(sys.stdin.readline())
l = sorted(list(map(int, sys.stdin.readline().split())))

left = 0
right = n-1
tmp = abs(l[left] + l[right])
res = [l[left], l[right]]

while left < right:
    summ = l[left] + l[right] 
    
    if abs(summ) < tmp:
        tmp = abs(summ)
        res = [l[left], l[right]]
        if tmp == 0:
            break
    
    if summ < 0:
        left += 1
    else:
        right -= 1
        
print(res[0], res[1])