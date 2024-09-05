def solution(n, left, right):
    # 시간초과 났대요~~
#     answer = []
#     board = [[0] * n for _ in range(n)]
#     for k in range(n): # 넣을 숫자 정하기 위해서
#         for i in range(k+1):
#             for j in range(k+1):
#                 if board[i][j] == 0:
#                     board[i][j] = k+1
#     print(board)
#     new_arr = []
    
#     for i in range(n):
#         for j in range(n):
#             new_arr.append(board[i][j])
    
#     return new_arr[left:right+1]

    answer = []
    for i in range(left, right+1):
        a = i // n
        b = i % n
        answer.append(max(a, b) + 1)
    return answer