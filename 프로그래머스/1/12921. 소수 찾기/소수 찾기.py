def is_prime(num):
    if num < 2:
        return 0
    cnt = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True

def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        if is_prime(i):
            answer += 1
        
            
    return answer