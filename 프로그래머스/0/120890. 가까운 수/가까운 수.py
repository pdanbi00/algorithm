def solution(array, n):
    answer = 0
    diff = 100
    array.sort()
    for i in range(len(array)):
        if diff > abs(n - array[i]):
            diff = abs(n-array[i])
            answer = array[i]
    return answer