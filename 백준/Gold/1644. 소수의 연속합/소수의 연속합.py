import math

n = int(input())

l = [False, False] + [True] * (n-1)
prime = []

for i in range(2, n+1):
    if l[i]:
        prime.append(i)
        for j in range(2*i, n+1, i):
            l[j] = False
            
ans = 0
left = 0
right = 0

while right <= len(prime):
    tmp = sum(prime[left:right])
    if tmp == n:
        ans += 1
        right += 1
    elif tmp < n:
        right += 1
    else:
        left += 1
        
print(ans)