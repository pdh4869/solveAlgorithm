def solution(rank, attendance):
    answer = 0
    tmp = []
    
    for i in range(len(attendance)):
        if attendance[i] == True:
            tmp.append([rank[i], i])
            
    tmp.sort(key = lambda x : x[0])

    answer = tmp[0][1] * 10000 + tmp[1][1] * 100 + tmp[2][1]
    return answer