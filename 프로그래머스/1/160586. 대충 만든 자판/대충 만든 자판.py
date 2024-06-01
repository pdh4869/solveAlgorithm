def solution(keymap, targets):
    answer = []
    
    for i in targets:
        tmp = 0
        for j in i:
            flag = False
            times = 101
            
            for k in keymap:
                if j in k:
                    times = min(k.index(j)+1, times)
                    flag = True
                
            if flag == False:
                tmp = -1
                break
                
            tmp += times
            
        answer.append(tmp)
    return answer