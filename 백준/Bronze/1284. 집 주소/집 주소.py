while True:
    cnt = 0
    n = input()
    
    if int(n) == 0:
        break
        
    for i in range(len(n)):
        cnt += 1
        if int(n[i]) == 1:
            cnt += 2
        elif int(n[i]) == 0:
            cnt += 4
        else:
            cnt += 3
    cnt += 1
    print(cnt)
    