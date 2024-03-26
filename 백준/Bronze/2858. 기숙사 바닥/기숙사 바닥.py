r,b = map(int, input().split())
z = r+b

for i in range(1, z+1):
    if (i-2) * (z // i - 2) == b:
        print(max(i, z//i), min(i, z//i))
        break