def solution(array):
    answer = 0
    N = len(array)
    for i in range(N):
        num = array[i]
        while num > 0:
            if num % 10 == 7:
                answer += 1
            num //= 10
    return answer