import sys
from collections import deque

input = sys.stdin.readline

# BFS를 도는데 i번째 플레이어는 move[i]번 만큼 bfs 도는거임.
# dr, dc를 movie[i]만큼 한번에 이동하는게 아님.

N, M, P = map(int, input().split())
move = list(map(int, input().split()))
board = [[] for _ in range(N)]

# 지도 초기화
for i in range(N):
    arr = list(input().rstrip())
    for a in arr:
        if a == '.' or a == '#':
            board[i].append(a)
        else:
            board[i].append(int(a))

# 각 플레이어가 갖고 있는 성 위치
p_castle = [[] for _ in range(P)]

# 방문 기록은 전체 한개 만들어놓고 계속 체크하면 됨.
visited = [[-1] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def sol(board, p_castle, distance, idx):
    q = deque()
    stack = [] # 여기에도 이동을 기록해서
    # 다음 차례에서는 내가 가진 모든 성을 도는게 아니라
    # 최근에 이동했던 성들을 도는거임. 그게 효율적이니깐

    cnt = 0 # 이번 판에 내가 확장한 성 개수


    while p_castle[idx]: # idx가 가지고 있는 성에서 다 돌아봐야 됨.
        pr, pc = p_castle[idx].pop()
        q.append((pr, pc, 0)) # 시작 거리는 0
        visited[pr][pc] = 0 # 이후 순서에서는 bfs 도는 동안 방문 표시가 될텐데
                            # 첫번째 순서에서는 기본 지도에서 1, 2 등등 인 곳들의 방문표시를 안했기 때문에 여기서 해줌.

    while q:
        r, c, dis = q.popleft()
        next_dis = dis + 1

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if next_dis > distance: # move[idx] 만큼 성 확장 했단 의미임
                break

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == '.' and visited[nr][nc] == -1:
                    if board[nr][nc] != idx:
                        cnt += 1
                        stack.append((nr, nc)) # 다음 차례에서 방문 시작할 곳들 파악하기 위해서도 넣기
                        q.append((nr, nc, next_dis)) # bfs 돌기 위해서 넣기
                        visited[nr][nc] = 0

    # 값 업데이트
    if cnt != 0:
        answer[idx] += cnt
        while stack:
            r, c = stack.pop()
            board[r][c] = idx # 지도에 성 표시
            p_castle[idx].append((r, c)) # 다음 차례에서 또 섬 확장해야하니깐
                                         # 어느 성에서 시작해서 확장할지 표시하기.
        return True
    return False

for i in range(N):
    for j in range(M):
        if board[i][j] != '.' and board[i][j] != '#':
            now_castle = board[i][j] - 1
            p_castle[now_castle].append((i, j))

# 정답값 기초로 만들어 놓기
answer = [0] * P
for idx in range(P):
    answer[idx] = len(p_castle[idx])

while 1: # 확장 더이상 못할 때까지 반복해야하니깐.
    impossible = True
    for ppp in range(P):
        check = sol(board, p_castle, move[ppp], ppp)
        if check:
            impossible = False
    if impossible:
        break
print(*answer)