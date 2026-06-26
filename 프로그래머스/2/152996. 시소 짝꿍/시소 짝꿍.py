def solution(weights):
    answer = 0
    
    info = dict()
    for w in weights:
        if w in info:
            info[w] += 1
        else:
            info[w] = 1
            
    for k, v in info.items():
        if v >= 2:
            answer += (v * (v-1)) // 2
    
    weights = set(weights)
    # 2:3, 2:4, 3:4 비율을 가지면 짝꿍 가능
    for w in weights:
        if w * 2 / 3 in weights:
            answer += info[w*2/3] * info[w]
        if w * 2 / 4 in weights:
            answer += info[w*2/4] * info[w]
        if w * 3 / 4 in weights:
            answer += info[w*3/4] * info[w]
    return answer