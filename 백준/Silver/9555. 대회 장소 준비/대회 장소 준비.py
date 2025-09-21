import sys
input = sys.stdin.readline
T = int(input())

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    school = set()
    for i in range(N):
        for j in range(M):
            if board[i][j] not in school and board[i][j] != -1:
                for k in range(8):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[i][j] == board[nr][nc]:
                            school.add(board[i][j])
                            break
    print(len(school))