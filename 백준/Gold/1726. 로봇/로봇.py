from collections import deque
M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
s_r, s_c, s_d = map(int, input().split())
e_r, e_c, e_d = map(int, input().split())
# 방향 1 : 동, 2 : 서, 3 : 남, 4 : 북

dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]

# bfs 돌면서 방향도 저장.
# 방향 차이 추가. for p in range(4) 할때 차이가 3이면 1로 바꿔서 넣기

# visited를 방향 따라서 3차원으로 만들기
def bfs():
    q = deque()
    q.append((s_r-1, s_c-1, s_d))
    # print(s_r-1, s_c-1, s_d-1)
    visited = [[[-1] * N for _ in range(M)] for _ in range(5)]
    visited[s_d][s_r-1][s_c-1] = 0
    while q:
        r, c, d = q.popleft()
        if r == (e_r - 1) and c == (e_c - 1) and d == (e_d):
            print(visited[d][r][c])
            break
        # 지금 방향 이어서 우선 이동
        for i in range(1, 4): # 방향
            nr = r + dr[d] * i
            nc = c + dc[d] * i
            if 0 <= nr < M and 0 <= nc < N:
                # 중간에 1이 껴있으면 이후에 2칸 이동하거나 3칸 이동하거나 등 더 멀리 갈 수 없음
                if board[nr][nc] == 1:
                    break
                if board[nr][nc] == 0 and visited[d][nr][nc] == -1:
                    visited[d][nr][nc] = visited[d][r][c] + 1
                    q.append((nr, nc, d))
        # 방향 전환 고려하기
        if d == 1 or d == 2: # 방향이 동쪽이거나 서쪽일 때
            if visited[3][r][c] == -1: # 남쪽 아직 방문 안했을 경우
                visited[3][r][c] = visited[d][r][c] + 1
                q.append((r, c, 3))
            if visited[4][r][c] == -1: # 북쪽 아직 방문 안했을 경우
                visited[4][r][c] = visited[d][r][c] + 1
                q.append((r, c, 4))
        else: # 방향이 남쪽이거나 북쪽일 때
            if visited[1][r][c] == -1: # 동쪽 아직 방문 안했을 경우
                visited[1][r][c] = visited[d][r][c] + 1
                q.append((r, c, 1))
            if visited[2][r][c] == -1: # 서쪽 아직 방문 안했을 경우
                visited[2][r][c] = visited[d][r][c] + 1
                q.append((r, c, 2))


bfs()
'''
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
2 4 1
'''
