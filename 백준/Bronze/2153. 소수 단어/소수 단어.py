def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = input()

cnt = 0
for i in b:
    cnt += a.index(i)
    


if is_prime(cnt) == True:
    print("It is a prime word.")
else:
    print("It is not a prime word.")