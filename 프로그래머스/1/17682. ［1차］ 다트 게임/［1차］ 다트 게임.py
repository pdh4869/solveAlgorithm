from collections import deque

def solution(dartResult):
    n = ''
    answer = []
    
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            answer.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            answer.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            answer.append(n)
            n = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * -1
            
    return sum(answer)
            