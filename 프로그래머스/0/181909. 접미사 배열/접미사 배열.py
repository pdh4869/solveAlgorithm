def solution(my_string):
    answer = []
    
    li = ['i','o','a','u','e']
    
    for i in range(len(my_string)):
        answer.append(my_string[i:])
        
    answer.sort()
    return answer