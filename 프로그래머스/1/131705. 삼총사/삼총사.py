def solution(number):
    answer = 0
    N = len(number)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                tmp = number[i] + number[j] + number[k]
                if tmp == 0:
                    answer += 1
    return answer