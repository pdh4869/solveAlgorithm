a = int(input())

for i in range(1,a):
    print(" "*(a-i)+'*' * (2*i-1))
    
for i in range(a,0,-1):
    print(" "*(a-i)+'*'*(2*i-1))