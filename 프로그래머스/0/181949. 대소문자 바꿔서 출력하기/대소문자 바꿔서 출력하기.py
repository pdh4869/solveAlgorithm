str = input()
str = list(str)

for i in range(len(str)):
    if ord(str[i]) < 97:
        str[i] = chr(ord(str[i]) + 32)
    else:
        str[i] = chr(ord(str[i]) - 32)

print(''.join(str))