def solution(a, b, c, d):
    answer = 0
    q = [a,b,c,d]
    z = dict()    
        
    for i in range(4):
        if q[i] not in z:
            z[q[i]] = 1
        else:
            z[q[i]] += 1

    maxx = max(z.values())
    minn = min(z.values())
    if maxx == 4:
        answer = max(z, key=z.get) * 1111
    elif maxx == 3:
        answer = (10 * max(z, key=z.get) + min(z, key=z.get)) ** 2
    elif maxx == 2 and minn == 2:
        tmp = [k for k,v in z.items() if max(z.values()) == v]
        answer = (tmp[0] + tmp[1]) * abs(tmp[0] - tmp[1])
    elif maxx == 2 and minn != 2:
        tmp = [k for k,v in z.items() if min(z.values()) == v]
        answer = tmp[0] * tmp[1]
    elif maxx == 1:
        answer = min(z.keys())
        
    return answer