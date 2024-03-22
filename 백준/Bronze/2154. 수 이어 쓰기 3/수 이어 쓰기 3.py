n = input()
a = ''

for i in range(1,100001):
    a += str(i)
    
print(a.index(n)+1)