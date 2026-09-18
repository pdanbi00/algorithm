from math import sqrt
def solution(number, limit, power):
    answer = 1
    divisor = set()
    for i in range(2, number+1):
        tmp = 2
        for j in range(2, int(sqrt(i))+1):
            if (i == j):
                continue
            if i % j == 0:
                tmp += 2
        num = int(sqrt(i))
        if (num * num == i):
            tmp -= 1
        # print(tmp)
        if tmp > limit:
            answer += power
        else:
            answer += tmp
            
    
    return answer