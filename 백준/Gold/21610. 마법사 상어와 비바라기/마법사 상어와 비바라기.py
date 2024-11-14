from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

dae_r = [-1, -1, 1, 1] # 단계 4에서 사용할 대각선들 방향
dae_c = [-1, 1, -1, 1] # 단계 4에서 사용할 대각선들 방향

clouds = deque()
clouds.append((N-2, 0))
clouds.append((N-2, 1))
clouds.append((N-1, 0))
clouds.append((N-1, 1))



def rain(direction, distance):
    # 이동했을 때 0보다 작게 되면 N-거리 만큼 더한 위치임
    # 이동했을 때 N-1보다 크게되면 거리 더한 값 % (N-1) 위치임.
    # for i in range(N):
    #     print(board[i])
    # print('---------')
    new_clouds = deque()
    while clouds:
        # 구름 이동시키기
        r, c = clouds.popleft()
        nr = r + (dr[direction] * distance)
        nc = c + (dc[direction] * distance)
        if nr < 0 or nr > N-1:
            nr = nr % N

        if nc < 0 or nc > N - 1:
            nc = nc % N
        board[nr][nc] += 1
        new_clouds.append((nr, nc))

    # print(new_clouds)
    # print('aaaaaaaaa')
    # for i in range(N):
    #     print(board[i])
    # print('bbbb')
    # 단계 4
    for i in range(len(new_clouds)):
        r, c = new_clouds[i]
        tmp = 0
        for k in range(4):
            nr = r + dae_r[k]
            nc = c + dae_c[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] > 0:
                    tmp += 1
        board[r][c] += tmp
    # print('구름 대각선 물 있는 곳 개수 추가')
    # for i in range(N):
    #     print(board[i])
    # print('cccccccccc')
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in new_clouds:
                clouds.append((i, j))
                board[i][j] -= 2


for _ in range(M):
    direction, distance = map(int, input().split())
    rain(direction-1, distance)
#
# print('최종 상태')
# for i in range(N):
#     print(board[i])

answer = 0

for i in range(N):
    for j in range(N):
        answer += board[i][j]
print(answer)