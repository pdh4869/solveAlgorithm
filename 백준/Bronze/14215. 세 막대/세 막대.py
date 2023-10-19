a = list(map(int, input().split()))
b = list(a)
max1 = max(a)
a.remove(max1)


while True:
    if max1 < sum(a):
        print(sum(a)+max1)
        break
    else:
        max1 -= 1
        if max1 < sum(a):
            print(sum(a)+max1)
            break