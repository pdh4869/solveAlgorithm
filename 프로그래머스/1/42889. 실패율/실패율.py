def solution(N, stages):
    answer = []
    
    fail = {}
    allPlayers = len(stages)
    
    for i in range(1, N+1):
        if allPlayers == 0:
            fail[i] = 0
        else:
            fail[i] = stages.count(i) / allPlayers
            allPlayers -= stages.count(i)
            
    answer = sorted(fail, key=lambda x:fail[x], reverse=True)
    return answer