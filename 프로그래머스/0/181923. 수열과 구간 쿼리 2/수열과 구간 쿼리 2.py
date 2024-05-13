def solution(arr, queries):
    answer = []
    
    for i in queries:
        tmp = []
        for j in range(i[0], i[1]+1):
            if arr[j] > i[2]:
                tmp.append(arr[j])
                
        if tmp == []:
            answer.append(-1)
        else:
            answer.append(min(tmp))
    return answer