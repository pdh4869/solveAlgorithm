def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        tmp = i[s:s+l]
        if int(tmp) > k:
            answer.append(int(tmp))
    return answer