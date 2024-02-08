a = input()
n = int(input())

li = sorted([input() for i in range(n)])
max_p = max_i = 0

for i in range(n):
    L = a.count('L') + li[i].count('L')
    O = a.count('O') + li[i].count('O')
    V = a.count('V') + li[i].count('V')
    E = a.count('E') + li[i].count('E')
    p = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    if max_p < p:
        max_p = p
        max_i = i
        
print(li[max_i])