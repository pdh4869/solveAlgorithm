def solution(num_list):
    answer = 0
    tmp = 1
    
    if len(num_list) >= 11:
        answer += sum(num_list)
    else:
        for i in range(len(num_list)):
            tmp *= num_list[i]
            
        answer += tmp
        
    return answer