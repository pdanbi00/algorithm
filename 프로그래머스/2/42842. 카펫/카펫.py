def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            w = yellow // i
            h = i
            if (w+2) * (h+2) == total:
                answer += [w+2, h+2]
    return answer