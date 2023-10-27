import sys

def recur(s,f,l):
    global cnt
    cnt += 1
    
    if f >= l: 
        return 1
    elif s[f] != s[l]: 
        return 0
    else: 
        return recur(s,f+1,l-1)
    
def isPal(s):
    return recur(s, 0, len(s)-1)
        
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    cnt = 0
    a = sys.stdin.readline().rstrip()
    print(isPal(a), cnt)   