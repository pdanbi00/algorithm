def solution(order):
    answer = 0
    while order > 0:
        tmp = order % 10
        if tmp == 3 or tmp == 6 or tmp == 9:
            answer += 1
        order //= 10
    return answer