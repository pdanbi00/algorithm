def solution(num, k):
    answer = -1
    cnt = 0

    while num > 0:
        tmp = num % 10
        if tmp == k:
            answer = cnt
        num //= 10
        cnt += 1
    if answer != -1:
        answer = cnt - answer
    return answer