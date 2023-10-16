a,b = input().split()
a = a[::-1]
cnt = 0

alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(a)):
    cnt += ((alp.index(a[i])) * (int(b) ** i))  

print(cnt)