def solution(myString, pat):
    answer = 0

    pat = pat.upper()
    myString = myString.upper()
    
    if pat in myString:
        answer += 1
        
    return answer