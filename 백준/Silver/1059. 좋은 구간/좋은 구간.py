s = int(input())
l = list(map(int, input().split()))
n = int(input())

l.append(0)
l.sort()

a = 0
for i in range(len(l)-1):
    if l[i] == n or l[i+1] == n:
        a = 0
        break
    elif l[i] < n < l[i+1]:
        a = (n - l[i]) * (l[i+1] - n) - 1
        break
    
print(a)        