import sys 
n = int(input())
sq = 2

while True:
    if (n == 1 or n == 2):
        print(n)
        break
    
    sq *= 2
    if sq >= n:
        print((n-(sq//2))*2)
        break