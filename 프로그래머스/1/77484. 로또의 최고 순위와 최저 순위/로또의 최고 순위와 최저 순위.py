def solution(lottos, win_nums):
    answer = []
    
    # 1등 6개, 5등 2개 
    cnt = 0  #최저
    cnt_zero = 0  # 0 개수
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        
        if lottos[i] == 0:
            cnt_zero += 1
            
    total = cnt + cnt_zero
    
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    answer = [rank[total], rank[cnt]]
    
    return answer