def solution(my_string, m, c):
    answer = ''
    
    for i in range(len(my_string)):
        if i % m == c-1:
            answer += my_string[i]
    return answer