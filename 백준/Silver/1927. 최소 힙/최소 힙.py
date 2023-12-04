import sys
import heapq as hq
n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap, x)
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap))
        else:
            print(0)