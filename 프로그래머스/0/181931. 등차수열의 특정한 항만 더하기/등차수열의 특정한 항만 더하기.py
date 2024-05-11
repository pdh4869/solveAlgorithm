def solution(a, d, included):
    answer = 0
    
    tmp = 0
    for i in range(len(included)):
        if i == 0:
            tmp += a
        else:
            tmp += d
            
        if included[i] == True:
            answer += tmp
            
    return answer