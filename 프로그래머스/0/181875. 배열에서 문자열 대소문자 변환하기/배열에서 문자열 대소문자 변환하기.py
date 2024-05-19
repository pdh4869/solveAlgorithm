def solution(strArr):
    answer = []
    
    for idx, value in enumerate(strArr):
        if idx % 2 == 1:
            answer.append(value.upper())
        else:
            answer.append(value.lower())
    return answer