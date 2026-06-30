def solution(x):
    answer = False
    tmp = 0
    num = x
    while num > 0:
        tmp += num % 10
        num //= 10
    if x % tmp == 0:
        answer = True
    return answer