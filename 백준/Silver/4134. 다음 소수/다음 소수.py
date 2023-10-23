import math
import sys

def prime(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
             return False
    
    return True
    
    
n = int(sys.stdin.readline())
for i in range(n):
    b = int(sys.stdin.readline())
    while True:
        if prime(b):
            print(b)
            break
        else:
            b += 1