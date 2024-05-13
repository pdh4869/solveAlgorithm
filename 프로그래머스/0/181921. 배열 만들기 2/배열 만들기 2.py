def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        tmp = str(i)
        if all(num in ["5", "0"] for num in tmp):
            answer.append(int(tmp))
        
    if answer == []:
        answer.append(-1)
    return answer