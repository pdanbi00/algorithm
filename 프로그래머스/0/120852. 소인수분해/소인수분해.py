import math
def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            possible = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    possible = False
                    break
            if possible:
                answer.append(i)
    return answer