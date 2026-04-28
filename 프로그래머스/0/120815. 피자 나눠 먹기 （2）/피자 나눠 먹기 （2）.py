def solution(n):
    answer = 0
    for i in range(6, 6 * n+1):
        if i % n == 0 and i % 6 == 0:
            answer = i // 6
            break
    return answer