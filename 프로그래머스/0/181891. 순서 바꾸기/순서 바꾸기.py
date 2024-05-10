def solution(num_list, n):
    answer = []
    
    answer.extend(num_list[n:])
    answer.extend(num_list[:n])
    return answer