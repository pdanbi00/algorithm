def solution(clothes):
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict:
            dict[cloth[1]].append(cloth[0])
        else:
            dict[cloth[1]] = [cloth[0]]
    answer = 1
    for k, v in dict.items():
        answer *= (len(v)+1)
    
    answer -= 1
    return answer