def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        a = X.count(str(i))
        b = Y.count(str(i))
        cnt = min(a, b)
        if cnt > 0:
            answer += str(i) * cnt
        
    if answer != '':
        if answer[0] == '0':
            answer = "0"
    else:
        answer = "-1"
    return answer