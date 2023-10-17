import math
a,b,c = map(int, input().split())

res = (c-b) / (a-b)
print(math.ceil(res))