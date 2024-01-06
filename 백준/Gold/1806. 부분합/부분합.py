import sys

n,s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))


left = 0
right = 0
leng = 100000
tmp = l[0]

while left <= right:
    if tmp >= s:
        leng = min(leng, right - left + 1)
        tmp -= l[left]
        left += 1
    else:
        right += 1
        if right < n:
            tmp += l[right]
        else:
            break

if leng == 100000:
    print(0)
else:
    print(leng)