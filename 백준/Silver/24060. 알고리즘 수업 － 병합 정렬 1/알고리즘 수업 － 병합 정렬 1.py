import sys

def msort(arr):
    if len(arr) < 2:
        return arr
    
    mid = (len(arr)+1) // 2
    low_arr = msort(arr[:mid])
    high_arr = msort(arr[mid:])
    
    mg_arr = []
    l,h = 0,0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            mg_arr.append(low_arr[l])
            res.append(low_arr[l])
            l += 1
        else:
            mg_arr.append(high_arr[h])
            res.append(high_arr[h])
            h += 1
    while l < len(low_arr):
        mg_arr.append(low_arr[l])
        res.append(low_arr[l])
        l += 1
    
    while h < len(high_arr):
        mg_arr.append(high_arr[h])
        res.append(high_arr[h])
        h += 1
    return mg_arr

a,b = map(int, sys.stdin.readline().rstrip().split())
c = list(map(int, sys.stdin.readline().rstrip().split()))
res = []
msort(c)

if len(res) >= b:
    print(res[b-1])
else:
    print(-1)