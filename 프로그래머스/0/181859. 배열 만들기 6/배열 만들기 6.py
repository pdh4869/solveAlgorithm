def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if answer == []:
            answer.append(arr[i])
        elif answer and answer[-1] == arr[i]:
            answer.pop()
        elif answer and answer[-1] != arr[i]:
            answer.append(arr[i])
            
            
    if answer == []:
        answer.append(-1)
    return answer