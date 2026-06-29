def solution(a, b):
    answer = 0
    t1 = min(a, b)
    t2 = max(a, b)
    for i in range(t1, t2+1):
        answer += i
    return answer