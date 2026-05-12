def solution(k, tangerine):
    answer = 0
    info = dict()
    for t in tangerine:
        if t in info:
            info[t] += 1
        else:
            info[t] = 1
            
    tanger = list(info.items())
    tanger.sort(key=lambda x : -x[1])
    
    for t in tanger:
        k -= t[1]
        answer += 1
        if k <= 0:
            break
    return answer