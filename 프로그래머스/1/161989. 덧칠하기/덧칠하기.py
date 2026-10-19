# from collections import deque
# def solution(n, m, section):
#     answer = 0
#     arr = deque(section)
    
#     while arr:
#         idx = arr.popleft()
#         size = idx + m - 1
#         answer += 1
#         while arr and arr[0] <= size:
#             arr.popleft()
#     return answer

def solution(n, m, section):
    answer = 1
    end = section[0] + m - 1
    
    for point in section:
        if point > end:
            answer += 1
            end = point + m - 1
    return answer