def solution(s):
    answer = 0
    
    sl = 0
    al = 0
    for i in range(len(s)):
        if sl == al:
            answer += 1
            x = s[i]
            
        if x == s[i]:
            sl += 1
        else:
            al += 1

    return answer