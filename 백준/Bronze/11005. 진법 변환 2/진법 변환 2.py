a,b = map(int, input().split())
m = ''
alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while a:
    m += str(alp[a%b])
    a = a // b
print(m[::-1])