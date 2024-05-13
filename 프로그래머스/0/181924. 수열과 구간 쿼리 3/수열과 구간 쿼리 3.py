def solution(arr, queries):
    answer = []
    
    for j in queries:
        tmp = arr[j[0]]
        arr[j[0]] = arr[j[1]]
        arr[j[1]] = tmp
    
    answer = arr
    return answer