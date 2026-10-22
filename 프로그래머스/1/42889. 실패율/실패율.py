def solution(N, stages):
    answer = []
    tmp = []
    stages.sort()
    idx = 0
    num = 1
    M = len(stages)
    
    while idx < M and num <= N:
        if stages[idx] == num:
            cnt = 0
            total = M - idx
                
            while idx < M and stages[idx] == num:
                cnt += 1
                idx += 1
            if total == 0:
                tmp.append((num, 0))
            else:
                tmp.append((num, cnt / total))
            num += 1
        else:
            tmp.append((num, 0))
            num += 1
            
    while num <= N:
        tmp.append((num, 0))
        num += 1
            
    tmp.sort(key=lambda x : (-x[1], x[0]))
    for i in range(N):
        answer.append(tmp[i][0])
    return answer