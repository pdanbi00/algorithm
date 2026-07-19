def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
    else:
        target = min(arr)
        for i in range(len(arr)):
            if arr[i] != target:
                answer.append(arr[i])
    return answer