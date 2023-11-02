n = int(input())
dic = {}

for i in range(n):
    a = input()
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

arr = []
for i,j in dic.items():
    if j == max(dic.values()):
        arr.append(i)
        
arr.sort()
print(arr[0])