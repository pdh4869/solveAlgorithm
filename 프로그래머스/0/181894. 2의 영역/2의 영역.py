def solution(arr):
    answer = []
    
    if 2 not in arr:
        answer.append(-1)
    else:
        tmp = []
        for index, value in enumerate(arr):
            if value == 2:
                tmp.append(index)
        answer.extend(arr[tmp[0]:tmp[-1]+1])
            
    return answer