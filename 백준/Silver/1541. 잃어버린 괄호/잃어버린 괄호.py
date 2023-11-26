# 잃어버린 괄호
exp = input().split('-')
s = 0

for i in exp[0].split('+'):
    s += int(i)
    
for i in exp[1:]:
    for j in i.split('+'):
        s -= int(j)
        
print(s)