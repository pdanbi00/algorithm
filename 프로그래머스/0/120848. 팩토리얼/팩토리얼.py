def solution(n):
    answer = 1
    num = 1
    while num < n:
        num *= answer
        if num >= n:
            if num > n:
                answer -= 1
            break
        answer += 1
    return answer