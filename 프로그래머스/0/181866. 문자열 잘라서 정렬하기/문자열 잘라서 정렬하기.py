def solution(myString):
    answer = []
    
    answer = [i for i in myString.split('x') if i]
    answer.sort()
    return answer