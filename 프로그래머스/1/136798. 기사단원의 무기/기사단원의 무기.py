def solution(number, limit, power):
    divisors = []
    answer = 0
    
    for i in range(1, number+1):
        divisor = 0
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0:
                divisor += 1
                if j ** 2 != i:
                    divisor += 1
            
            if divisor > limit:
                divisor = power
                break
                
        divisors.append(divisor)
    return sum(divisors)
