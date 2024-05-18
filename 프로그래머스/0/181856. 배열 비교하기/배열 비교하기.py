def solution(arr1, arr2):
    answer = 0
    
    a = len(arr1)
    b = len(arr2)
    
    
    if a != b:
        if a > b:
            answer = 1
        else:
            answer = -1
    else:
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1
        elif sum(arr1) == sum(arr2):
            answer = 0
    return answer