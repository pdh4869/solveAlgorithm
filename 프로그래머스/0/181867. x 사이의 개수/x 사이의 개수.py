def solution(myString):
    answer = []
    
    tmp = 0
    for i in myString:
        if i == 'x':
            answer.append(tmp)
            tmp = 0
        else:
            tmp += 1
            
    if myString[-1] == 'x':
        answer.append(0)
    else:
        answer.append(tmp)
    return answer