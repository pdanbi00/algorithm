def solution(keymap, targets):
    answer = []
    info = dict()
    for key in keymap:
        for i in range(len(key)):
            if key[i] in info:
                info[key[i]] = min(i+1, info[key[i]])
            else:
                info[key[i]] = i+1
    
    for target in targets:
        cnt = 0
        for i in range(len(target)):
            if target[i] not in info:
                cnt = -1
                break
            cnt += info[target[i]]
        answer.append(cnt)
    return answer