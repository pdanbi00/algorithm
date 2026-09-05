def solution(s):
    answer = ''
    info = dict()
    N = len(s)
    for i in range(N):
        if s[i] not in info:
            info[s[i]] = 1
        else:
            info[s[i]] += 1
            
    for k, v in info.items():
        if v == 1:
            answer += k
    arr = sorted(list(answer))
    return ''.join(arr)