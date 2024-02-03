n = input()
f = int(input())
tmp = int(n[:-2] + "00")

while True:
    if tmp % f == 0:
        print(str(tmp)[-2:])
        break
    
    tmp += 1