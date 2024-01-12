def solution(clothes):
    
    dic = {}
    wear = set()
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
            wear.add(cloth[1])
        else:
            dic[cloth[1]] += 1
    wear = list(wear)
    total = 1
    for w in wear:
        total *= dic[w] + 1
    return total - 1
    # answer = 0
    # return answer