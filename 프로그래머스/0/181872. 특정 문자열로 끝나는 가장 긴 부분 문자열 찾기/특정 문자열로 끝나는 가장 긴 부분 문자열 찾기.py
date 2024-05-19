def solution(myString, pat):
    answer = myString[:myString.rfind(pat)+len(pat)]
    return answer