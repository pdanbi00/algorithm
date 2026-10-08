def solution(s):
    answer = []
    info = dict()
    
    N = len(s)
    for i in range(N):
        if s[i] not in info:
            answer.append(-1)
        else:
            answer.append(i-info[s[i]])
            
        info[s[i]] = i
        
    return answer