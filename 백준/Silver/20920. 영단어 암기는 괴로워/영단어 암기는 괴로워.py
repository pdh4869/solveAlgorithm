import sys

a,b = map(int, sys.stdin.readline().rstrip().split())
l = {}
for i in range(a):
    z = sys.stdin.readline().rstrip()
    if len(z) >= b:
        if z in l:
            l[z] += 1
        else:
            l[z] = 1
            
ll = sorted(l.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in ll:
    print(i[0])