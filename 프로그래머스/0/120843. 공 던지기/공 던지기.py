def solution(numbers, k):
    answer = numbers[(k-1) * 2  % len(numbers)]
    return answer