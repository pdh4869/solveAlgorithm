def facto(n):
    if n == 0:
        return 1
    
    return n * facto(n-1)

n = int(input())
print(facto(n))
