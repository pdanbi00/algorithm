# 핀을 움직였다면 핀은 하나 사라짐
# 핀을 움직인 횟수 = 핀을 없앤 횟수

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(movetime): # 움직임마다 변하는 보드 구현 함수
    global min_move, min_cnt

    # 핀 위치 저장
    pins = []
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                pins.append((i, j))

    if len(pins) < min_cnt:
        min_move = movetime # 가장 적은 움직임 갱신
        min_cnt = len(pins) # 가장 적은 핀의 개수 갱신

        # 제일 처음 핀의 수를 세놓았으면
        # 맨 처음 핀의 수 - 가장 적게 남은 핀의 수 = 최소 이동횟수
        # 핀의 이동횟수 = 제거한 핀의 수
    for r, c in pins:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 인접 칸 다음 칸도 고려해야 됨.
            # 인접 칸 뛰어넘어서도 움직일 수 있으면
            if 0 <= nr + dr[k] < 5 and 0 <= nc + dc[k] < 9:
                if board[nr][nc] == 'o' and board[nr + dr[k]][nc + dc[k]] == '.':
                    # 인접한 핀 뛰어 넘었으면 핀 지우고 새로운 board에서 다음 함수 실행
                    board[nr][nc] = '.'
                    board[nr + dr[k]][nc + dc[k]] = 'o'
                    board[r][c] = '.'
                    move(movetime+1)
                    board[nr][nc] = 'o'
                    board[nr + dr[k]][nc + dc[k]] = '.'
                    board[r][c] = 'o'
T = int(input())
for i in range(T):
    min_cnt = 10
    min_move = 10
    board = [list(input().rstrip()) for _ in range(5)] # 게임판은 모두 같은 모양을 가진다고 했음. 9 * 5
    if i < T-1:
        input() # 빈칸 처리
    move(0)
    print(min_cnt, min_move)
