from collections import deque

N, K = map(int, input().split())
board = [(list(map(int, input())) + [1] * K) for _ in range(2)]

visited = [[-1] * (N+K) for _ in range(2)]
q = deque()
l_r = 0
q.append((l_r, 0, 0)) # 방향, 몇 번째 칸인지, 시간
visited[l_r][0] = 0
d = [1, -1, K]
answer = 0
while q:
    directions, idx, time = q.popleft()
    if idx > N-1:
        answer = 1
        break
    for k in range(2):
        next_idx = idx + d[k]
        if next_idx > time:
            if 0 <= next_idx and board[directions][next_idx] == 1 and visited[directions][next_idx] == -1:
                visited[directions][next_idx] = time + 1
                q.append((directions, next_idx, time+1))
    # 반대편 줄로 이동하는 경우
    next_idx = idx + d[2]
    directions += 1
    directions %= 2
    if next_idx > time:
        if 0 <= next_idx and board[directions][next_idx] == 1 and visited[directions][next_idx] == -1:
            visited[directions][next_idx] = time + 1
            q.append((directions, next_idx, time + 1))
# print(visited)
print(answer)