def solution(binomial):
    answer = 0
    
    binomial = binomial.split(' ')
    print(binomial)
    
    a = int(binomial[0])
    b = binomial[1]
    c = int(binomial[2])
    
    if b == '+':
        answer = a + c
    elif b == '-':
        answer = a - c
    elif b == '*':
        answer = a * c

    return answer