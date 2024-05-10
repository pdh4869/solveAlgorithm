def solution(a, b):
    answer = 0
    
    e1 = 2 * a * b
    e2 = int(str(a) + str(b))
    
    if e1 > e2:
        answer = e1
    else:
        answer = e2
    return answer