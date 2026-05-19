def solution(array):
    answer = []
    N = len(array)
    max_v = 0
    idx = 0
    for i in range(N):
        if array[i] > max_v:
            max_v = array[i]
            idx = i
    return [max_v, idx]