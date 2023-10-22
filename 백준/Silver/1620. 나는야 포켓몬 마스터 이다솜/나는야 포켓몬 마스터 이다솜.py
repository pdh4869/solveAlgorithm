import sys

a,b = map(int, sys.stdin.readline().split())
dic1 = {}
dic2 = {}

for i in range(1,a+1):
    d = sys.stdin.readline().rstrip()
    dic1[i] = d
    dic2[d] = i
    
    
for i in range(b):
    q = sys.stdin.readline().rstrip()
    if q.isdigit() == True:
        print(dic1[int(q)])
    else:
        print(dic2[q])