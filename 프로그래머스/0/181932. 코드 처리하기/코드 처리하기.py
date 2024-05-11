def solution(code):
    answer = ''
    mode = False
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
        else:
            if mode == False:
                if i % 2 == 0:
                    answer += code[i]
            elif mode == True:
                if i % 2 == 1:
                    answer += code[i]
    return answer if answer != '' else "EMPTY"