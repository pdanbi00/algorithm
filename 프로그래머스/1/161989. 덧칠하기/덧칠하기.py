from collections import deque
def solution(n, m, section):
    answer = 0
    arr = deque(section)
    
    while arr:
        idx = arr.popleft()
        size = idx + m - 1
        answer += 1
        while arr and arr[0] <= size:
            arr.popleft()
    return answer