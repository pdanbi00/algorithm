def solution(n, s):
    answer = []
    tmp = s // n
    if tmp == 0:
        answer = [-1]
    else:
        answer = [tmp] * n
        if s % n > 0:
            for i in range(s%n):
                answer[n-1-i] += 1
    return answer