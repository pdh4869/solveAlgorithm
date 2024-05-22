def solution(arr):
    answer = 0
    
    a = len(arr)
    b = len(arr[0])
    
    for i in range(a):
        for j in range(b):
            if arr[i][j] == arr[j][i]:
                answer += 1
            
    if answer == a * b:
        return 1
    else: return 0