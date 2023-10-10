a,b = map(int, input().split())
basket = [i for i in range(1,a+1)]
tmp = 0 

for x in range(b):
    i,j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp

for i in basket:
    print(i, end=' ')