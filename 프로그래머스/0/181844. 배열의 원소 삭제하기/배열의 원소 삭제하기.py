def solution(arr, delete_list):
    answer = []
    rm = []
    
    for i in arr:
        for j in delete_list:
            if i == j:
                rm.append(i)
                arr = [x for x in arr if x not in rm]
                
    answer = arr
    return answer