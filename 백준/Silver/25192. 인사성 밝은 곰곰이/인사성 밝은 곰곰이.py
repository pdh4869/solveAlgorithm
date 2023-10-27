n = int(input())
dic = {}
cnt = 0
for i in range(n):
    a = input()
    if a != "ENTER":
        if a not in dic.keys():
            dic[a] = 1
            cnt += 1
    else:
        dic.clear()

print(cnt)