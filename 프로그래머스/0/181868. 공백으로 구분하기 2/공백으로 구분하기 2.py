def solution(my_string):
    answer = []
    my_string = my_string.strip()
    answer = my_string.split(' ')
    
    answer = ' '.join(answer).split()

    return answer