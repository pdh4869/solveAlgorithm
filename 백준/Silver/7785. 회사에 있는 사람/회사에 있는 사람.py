a = int(input())
dic = {}

for i in range(a):
    b,c = map(str, input().split())
    if c == "enter":
        dic[b] = 1
    else:
        dic[b] = 0

d1 = dict(sorted(dic.items(), reverse=True))

for i in d1:
    if d1[i] == 1:
        print(i)