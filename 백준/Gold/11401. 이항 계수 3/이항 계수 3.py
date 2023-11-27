import sys 
n,k = map(int, sys.stdin.readline().split())
p = 1000000007

def factorial(n):
    num = 1
    for i in range(2, n+1):
        num = (num * i) % p
    return num

def square(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n,k//2)
    if k % 2:
        return (tmp * tmp * n) % p
    else:
        return (tmp * tmp) % p
    
top = factorial(n)
bot = factorial(n-k) * factorial(k) % p

print(top * square(bot, p-2) % p)