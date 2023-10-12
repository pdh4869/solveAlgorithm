rating = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

tot = 0
result = 0

for i in range(20):
    a,b,c = input().split()
    b = float(b)
    if c != 'P':
        tot += b
        result += score[rating.index(c)] * b

print("%.6f" % (result / tot))