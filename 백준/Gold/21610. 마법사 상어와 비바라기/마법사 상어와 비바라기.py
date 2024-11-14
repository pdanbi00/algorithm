import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [list(map(int, input().split())) for _ in range(M)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
for direction in directions:
    d, m = direction[0] - 1, direction[1] % N
    not_cloud = set()
    while clouds:
        r, c = clouds.pop()
        nr = (r + (dr[d] * m)) % N
        nc = (c + (dc[d] * m)) % N
        board[nr][nc] += 1
        # 구름 있던 자리는 저장했다가 나중에 제외시키기
        not_cloud.add((nr, nc))

    # 물 뿌리기
    for nr, nc in not_cloud:
        count = 0
        for k in [1, 3, 5, 7]:
            nnr = nr + dr[k]
            nnc = nc + dc[k]
            if 0 <= nnr < N and 0 <= nnc < N:
                if board[nnr][nnc] > 0:
                    count += 1
        board[nr][nc] += count

    # 새로운 구름 만들기
    for i in range(N):
        for j in range(N):
            if (i, j) not in not_cloud:
                if board[i][j] >= 2:
                    clouds.append((i, j))
                    board[i][j] -= 2
answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]
print(answer)