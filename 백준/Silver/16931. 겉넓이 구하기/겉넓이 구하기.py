N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 다 1부터 넣을거임
real = [[[False] * 102 for _ in range(M+2)] for _ in range(N+2)]
# real[i][j][k] : i행 j열 칸에 k번째높이에 블록이 쌓여있는지
# 블록 3차원으로 쌓기
for i in range(N):
    for j in range(M):
        cnt = board[i][j]
        for k in range(1, cnt+1):
            real[i+1][j+1][k] = True
# 사각형 하나 기준으로 6방향으로 보면서 맞닿아 있는거 없으면 답에 1 추가
# 위, 아래, 오른쪽, 왼쪽, 앞, 뒤
dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

ans = 0
# 정육면체 하나씩 잡고 6방향으로 맞닿은거 있는지 확인
for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, board[i-1][j-1]+1):
                for p in range(6):
                    nr = i + dr[p]
                    nc = j + dc[p]
                    nz = k + dz[p]
                    if real[nr][nc][nz] == False:
                        ans += 1
print(ans)