def solution(want, number, discount):
    answer = 0
    want_info = dict()
    N = len(want)
    for i in range(N):
        want_info[want[i]] = number[i]
    
    M = len(discount)
    
    for i in range(M-9):
        tmp = dict()
        possible = True
        for j in range(10):
            if discount[i+j] not in want:
                possible = False
                break
                
            else:
                if discount[i+j] in tmp:
                    tmp[discount[i+j]] += 1
                    if tmp[discount[i+j]] > want_info[discount[i+j]]:
                        possible = False
                        break
                else:
                    tmp[discount[i+j]] = 1
        if possible:
            for k, v in want_info.items():
                if tmp[k] != v:
                    possible = False
                    break
                    
        if possible:
            answer += 1
        
    return answer