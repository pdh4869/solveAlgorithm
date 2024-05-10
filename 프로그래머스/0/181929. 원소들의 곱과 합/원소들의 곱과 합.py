from functools import reduce

def solution(num_list):
    answer = 0
    
    product = lambda num_list: reduce(lambda x, y: x * y, num_list)
    if product(num_list) < sum(num_list) ** 2:
        answer = 1    
    else:
        answer = 0
        
    return answer