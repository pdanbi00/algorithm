def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for m in moves:
        # c = m-1
        idx = 0
        while idx < N and board[idx][m-1] == 0 :
            idx += 1

        if idx < N:
            tmp = board[idx][m-1]
            # print(tmp)
            board[idx][m-1] = 0
            if not stack:
                stack.append(tmp)
            else:
                if stack[-1] == tmp:
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(tmp)
    return answer