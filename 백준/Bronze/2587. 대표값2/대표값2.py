b = []
summ = 0
for i in range(5):
    a = int(input())
    b.append(a)
    
b.sort()

for i in b:
    summ += i
    
print(summ//5)
print(b[2])