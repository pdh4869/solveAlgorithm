def solution(n, slicer, num_list):
    answer = []
    
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    if n == 1:
        answer = num_list[0:b+1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b+1]
    elif n == 4:
        for i in range(a,b+1,c):
            answer.append(num_list[i])
    
    return answer