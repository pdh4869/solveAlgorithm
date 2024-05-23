import math
def solution(arr):
    answer = arr
    i = 0
    while len(answer) != 2 ** i:
        if len(answer) == 2 ** i:
            break
            
        if len(answer) > 2 ** i:
            i += 1
        else:
            answer = arr + [0] * ((2 ** i) - len(answer))
    return answer