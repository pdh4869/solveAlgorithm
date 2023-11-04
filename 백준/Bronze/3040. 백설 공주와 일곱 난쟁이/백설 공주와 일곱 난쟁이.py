from itertools import combinations

for i in combinations([int(input()) for i in range(9)],7):
  if sum(i) == 100:
    for j in sorted(i):
      print(j)
