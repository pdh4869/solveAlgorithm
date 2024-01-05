import sys

n = int(input())
a = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

cnt = 0
left = 0
right = n-1

while left < right:
    tmp = a[left] + a[right]
    if tmp == x:
        cnt += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1
        
print(cnt)