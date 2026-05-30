import math
def solution(enroll, referral, seller, amount):
    answer = []
    info_money = dict()
    info_relate = dict()
    M = len(enroll)
    for i in range(M):
        info_relate[enroll[i]] = referral[i]
    
    for e in enroll:
        info_money[e] = 0
        
    N = len(seller)
    
    for i in range(N):
        total = amount[i] * 100
        one = math.trunc(total * 0.1)
        nine = total - one
        
        info_money[seller[i]] += nine
        tmp = one
        if tmp < 1:
            continue
        sub = info_relate[seller[i]]
        if sub == '-':
            continue
        while tmp >= 1:
            sup = info_relate[sub]
            one = math.trunc(tmp * 0.1)
            nine = tmp - one
            if sup == '-':
                if one < 1:
                    info_money[sub] += tmp
                else:
                    info_money[sub] += nine
                break
            else:
                if one < 1:
                    info_money[sub] += tmp
                    break
                else:
                    info_money[sub] += nine
                    tmp = one
                    sub = sup

    for e in enroll:
        answer.append(info_money[e])
    return answer