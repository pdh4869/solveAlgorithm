def solution(num_list):
    answer = 0
    e1 = 0
    e2 = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            e1 += num_list[i]
        else:
            e2 += num_list[i]
            
    if e1 > e2:
        answer = e1
    else:
        answer = e2
    return answer