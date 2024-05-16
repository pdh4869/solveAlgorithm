def solution(my_string):
    answer = []
    
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
               'q','r','s','t','u','v','w','x','y','z']
    
    
    z = dict()
    for i in my_string:
        if i not in z:
            z[i] = 1
        else:
            z[i] += 1
    
    for i in alphabet:
        if i not in z:
            answer.append(0)
        else:
            answer.append(z[i])
    
    return answer