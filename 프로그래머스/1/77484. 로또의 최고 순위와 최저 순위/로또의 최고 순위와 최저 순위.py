def solution(lottos, win_nums):
    answer = []
    zero = 0
    cnt = 0
    for l in lottos:
        if l == 0:
            zero += 1
        elif l in win_nums:
            cnt += 1
    
    first = zero + cnt
    if first <= 1:
        answer.append(6)
    else:
        answer.append(7 - first)
        
    second = cnt
    if second <= 1:
        answer.append(6)
    else:
        answer.append(7 - second)
    return answer