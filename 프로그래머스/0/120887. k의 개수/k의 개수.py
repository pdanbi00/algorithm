def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        while a > 0:
            tmp = a % 10
            if tmp == k:
                answer += 1
            a //= 10
    return answer