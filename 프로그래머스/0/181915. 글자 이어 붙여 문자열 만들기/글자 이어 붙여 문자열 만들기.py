def solution(my_string, index_list):
    answer = ''
    i = 0
    
    while i < len(index_list):
        answer += my_string[index_list[i]]
        i += 1
        
    return answer