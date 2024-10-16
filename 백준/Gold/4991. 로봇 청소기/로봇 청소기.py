# 아이디어
# 청소기에서부터 각 먼지들까지의 거리를 구함
# 각 먼지들의 거리를 구함
# 순열을 통해서 청소할 먼지의 순서를 섞음
# 최솟값 비교
from collections import deque
from itertools import permutations

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0:
                    if board[nr][nc] != 'x':
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1
    return visited

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    board = []
    dust = []
    robot_r = 0
    robot_c = 0
    for i in range(N):
        arr = list(input().strip())
        for j in range(M):
            if arr[j] == 'o':
                robot_r = i
                robot_c = j
            elif arr[j] == '*':
                dust.append((i, j))
        board.append(arr)

    cleaner = [0] * len(dust) # 로봇청소기 ~ 먼지까지의 거리
    visited = bfs(robot_r, robot_c)
    possible = True # 로봇 청소기가 모든 더러운 칸을 방문할 수 있는지 여부
    for idx, location in enumerate(dust):
        temp = visited[location[0]][location[1]]
        if temp == 0: # 더러운 곳 중 로봇청소기가 방문할 수 없는 곳이 있다면
            print(-1)
            possible = False
            break
        cleaner[idx] += temp-1 # 거리니깐 bfs돌때 처음 로봇청소기 위치 1로 두는게 빼기

    if possible:
        distance = [[0] * len(dust) for _ in range(len(dust))] # 더러운칸 사이의 거리
        for i in range(len(distance)-1):
            visited = bfs(dust[i][0], dust[i][1])
            for j in range(i+1, len(distance)):
                distance[i][j] = visited[dust[j][0]][dust[j][1]] - 1
                distance[j][i] = distance[i][j]
        answer = int(1e9)
        for perm in permutations(range(len(distance))): # 순열 사용해서 최적 순서 찾기
            temp = cleaner[perm[0]]
            start = perm[0]
            for idx in range(1, len(perm)):
                end = perm[idx]
                temp += distance[start][end]
                start = end
            answer = min(answer, temp)
        print(answer)



    q = deque()
    visited = [[0] * M for _ in range(N)]
