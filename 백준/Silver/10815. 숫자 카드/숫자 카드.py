a = int(input())
a_list = list(map(int, input().split()))
b = int(input())
b_list = list(map(int, input().split()))

dic = {}

for i in b_list:
    dic[i] = 0
    
for i in a_list:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end=' ')