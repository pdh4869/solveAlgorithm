import sys

a,b = map(int, sys.stdin.readline().split())
cnt = 0
dic = {}

for i in range(a):
    dic[sys.stdin.readline()] = 1

for i in range(b):
    data = sys.stdin.readline()
    if data in dic:
        cnt += 1
    
print(cnt)