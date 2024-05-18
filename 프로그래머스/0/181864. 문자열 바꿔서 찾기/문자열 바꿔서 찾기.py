def solution(myString, pat):
    answer = 0
    tmp = ''
    for i in myString:
        if i == 'A':
            tmp += 'B'
        elif i == 'B':
            tmp += 'A'
            
    if pat in tmp:
        answer += 1
    return answer