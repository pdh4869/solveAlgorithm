a,b,c = map(int, input().split())
l = [0] * a

cnt = 0
i = 0

while l[i] < b-1:
    l[i] += 1
    cnt += 1
    i = (i+c) % a if l[i] % 2 == 1 else (i-c) % a
print(cnt)