def solution(myStr):
    answer = []
    
    tmp = ''
    for i in ['a','b','c']:
        myStr = myStr.replace(i, ' ')
        
    answer = myStr.split()
    
    if answer == []:
        answer.append("EMPTY")
        
    return answer