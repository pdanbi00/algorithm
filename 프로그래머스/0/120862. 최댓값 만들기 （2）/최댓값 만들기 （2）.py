def solution(numbers):
    answer = 0
    numbers.sort()
    tmp1 = numbers[-1] * numbers[-2]
    tmp2 = numbers[0] * numbers[1]
    return max(tmp1, tmp2)