import math

def prime(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
             return False
    
    return True

limit_list = list(range(2,246912))
check = []
for i in limit_list:
    if prime(i): check.append(i)
        
while True:
    cnt = 0
    a = int(input())
    if a == 0: break
    
    for i in check:
        if a < i <= 2*a:
            cnt += 1
    print(cnt)