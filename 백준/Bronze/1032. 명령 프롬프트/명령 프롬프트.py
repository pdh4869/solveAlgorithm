n = int(input())
first = list(input())
first_len = len(first)

for i in range(n-1):
    other = list(input())
    for j in range(first_len):
        if first[j] != other[j]:
            first[j] = '?'
    
print(''.join(first))