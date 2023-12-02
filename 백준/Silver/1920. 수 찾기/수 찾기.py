import sys 
n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
nl.sort()

m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))

def bsearch(target):    
    start = 0
    end = n-1
    
    while start <= end:
        mid = (start+end) // 2
        if nl[mid] == target:
            return True
        
        if target < nl[mid]:
            end = mid - 1
        elif target > nl[mid]:
            start = mid + 1

for i in range(m):
    if bsearch(ml[i]):
        print(1)
    else:
        print(0)