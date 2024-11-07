# 한 방향으로 계속 진행해야 됨
# 최소 방향 전환 몇번 했는지 출력
import sys
sys.setrecursionlimit(10**9)
case = 1 # 테스트케이스 번호 출력용

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# board 탐색하면서 모든 좌표 지나갔는지 확인
def check():
    for i in range(N):
        for j in range(M):
            if board[i][j] == '.':
                return False
    return True

# 백트래킹
# answer보다 현재 탐색중인 횟수 cnt가 작으면 다음 경로 탐색
# 2차원 배열인 board를 deepcopy해서 매개변수 전달 안하려고 지나간 좌표들 저장해놓고 탐색 끝나면 다시 '.'로 돌려주기
def bt(r, c, cnt):
    global answer
    if check(): # 모든 좌표 다 탐색한 경우
        answer = min(answer, cnt)
    if cnt < answer: # 현재까지 탐색한 경로수가 answer보다 작을때만 탐색
        for d in range(4):
            tmp = [] # 지나온 좌표 담기
            nr = r
            nc = c
            while True:
                nr += dr[d]
                nc += dc[d]
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '.':
                    tmp.append((nr, nc))
                    board[nr][nc] = '*'
                else:
                    break
            if tmp:
                bt(nr - dr[d], nc - dc[d], cnt + 1)
            for a, b in tmp:
                board[a][b] = '.'
        board[r][c] = '.'


while True:
    try:
        N, M = map(int, input().split())
        visited = [[False] * M for _ in range(N)]
        board = [list(input().rstrip()) for _ in range(N)]
        answer = 1e9
        for i in range(N):
            for j in range(M):
                if board[i][j] == '.': # 구슬을 놓을 수 있으면 그 자리에 구슬 놓고 시작
                    board[i][j] = '*'
                    bt(i, j, 0)
        if answer == 1e9:
            answer = -1
        print(f'Case {case}: {answer}')
        case += 1
    except:
        break