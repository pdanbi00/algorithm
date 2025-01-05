board = []
empty = [] # 채워야하는 위치 기억하기
ans = []
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] == 0:
            arr[j] = -1
            empty.append((i, j))
    board.append(arr)

def dfs(nums, board):
    global ans
    if len(nums) == 0:
        ans = board
        # for i in range(9):
        #     for j in range(9):
        #         if j != 8:
        #             print(board[i][j], end = ' ')
        #         else:
        #             print(board[i][j])
        return
    r = nums[0][0]
    c = nums[0][1]
    for n in range(1, 10):
        possible = True
        board[r][c] = n
        # 가로 확인
        for j in range(9):
            if j != c:
                if board[r][j] == board[r][c]:
                    possible = False
                    break
        # 세로 확인
        if possible:
            for i in range(9):
                if i != r:
                    if board[i][c] == board[r][c]:
                        possible = False
                        break
        # else:
        #     continue
        # 3 X 3 확인
        if possible:
            r_tmp = (r // 3) * 3
            c_tmp = (c // 3) * 3
            for i in range(3):
                for j in range(3):
                    if r_tmp + i != r and c_tmp + j != c:
                        if board[r_tmp+i][c_tmp+j] == board[r][c]:
                            possible = False
                            break
        # else:
        #     continue
        # 가로, 세로, 3 X 3 다 겹치는게 없다면 다음 단계로
        if possible:
            dfs(nums[1:], board)
            if ans:
                return
        board[r][c] = 0
    return

dfs(empty, board)
for i in range(9):
    for j in range(9):
        if j != 8:
            print(ans[i][j], end = ' ')
        else:
            print(ans[i][j])

'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''