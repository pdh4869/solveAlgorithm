a = int(input())

for i in range(1,a+1):
    n = sum(map(int, str(i)))
    n_sum = i+n
    
    if n_sum == a:
        print(i)
        break
    
    if i == a:
        print(0)