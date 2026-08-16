def solution(t, p):
    answer = 0
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        tmp = int(t[i:i+M])
        # print(tmp)
        if int(tmp) <= int(p):
            answer += 1
    return answer