def solution(picture, k):
    answer = []
    for i in picture:
        tmp = ''
        for j in i:
            tmp += j * k
        answer.extend([tmp] * k)
    return answer