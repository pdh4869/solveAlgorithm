def solution(myString):
    answer = ''
    
    for i in myString:
        if i == 'a':
            answer += 'A'
        elif i != 'A' and ord(i) < 97:
            answer += i.lower()
        else:
            answer += i
    return answer