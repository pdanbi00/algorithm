from collections import deque
N = int(input())
board = []
doors = []
for i in range(N):
    arr = list(input())
    for j in range(N):
        if arr[j] == '#':
            doors.append((i, j))
    board.append(arr)

sr, sc = doors[0]
er, ec = doors[1]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[[-1] * 4 for _ in range(N)] for _ in range(N)]

def bfs():
    q = deque()
    # 시작점 4방향 q 삽입 및 방문처리
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        # 4방향에서 다음으로 진출할 수 있는 경우만
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != '*':
            visited[sr][sc][k] = 0
            q.append((sr, sc, k))

    while q:
        r, c, d = q.popleft()
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            # 1. 빈칸 혹은 문일 경우
            if board[nr][nc] == '.' or board[nr][nc] == '#':
                # 방문한 적 없으면
                if visited[nr][nc][d] == -1:
                    q.append((nr, nc, d)) # 방향 유지
                    visited[nr][nc][d] = visited[r][c][d]
                # 방문한적 있을 경우 더 적은 거울 사용하는 경우만 업데이트
                else:
                    if visited[nr][nc][d] > visited[r][c][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = visited[r][c][d]
            # 2. 거울을 설치할 수 있는 곳이면
            elif board[nr][nc] == '!':
                # 거울 설치 안하는 경우
                # 방문한 적 없으면
                if visited[nr][nc][d] == -1:
                    q.append((nr, nc, d)) # 방향 유지
                    visited[nr][nc][d] = visited[r][c][d]
                # 방문한적 있을 경우 더 적은 거울 사용하는 경우만 업데이트
                else:
                    if visited[nr][nc][d] > visited[r][c][d]:
                        q.append((nr, nc, d))
                        visited[nr][nc][d] = visited[r][c][d]

                # 거울을 설치하는 경우
                for new_d in [(d+1) % 4, (d+3) % 4]:
                    # 방문한 적 없으면
                    if visited[nr][nc][new_d] == -1:
                        q.append((nr, nc, new_d))
                        visited[nr][nc][new_d] = visited[r][c][d] + 1
                    # 방문한적 있을 경우 더 적은 거울 사용하는 경우만 업데이트
                    else:
                        if visited[nr][nc][new_d] > visited[r][c][d] + 1:
                            q.append((nr, nc, new_d))
                            visited[nr][nc][new_d] = visited[r][c][d] + 1
    ans = 1e9
    # 최소 거울 개수 찾기
    for cnt in visited[er][ec]:
        if cnt == -1:
            continue
        ans = min(ans, cnt)
    print(ans)

bfs()