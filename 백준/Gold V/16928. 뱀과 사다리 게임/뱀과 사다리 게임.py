from collections import deque
board = [0] * 101
visited = [False] * 101
N, M = map(int, input().split())
ladder = {}
snake = {}
q = deque()
for i in range(N):
    s, e = map(int, input().split())
    ladder[s] = e
for j in range(M):
    s, e = map(int, input().split())
    snake[s]= e

q.append(1)
visited[1] = True
while q:
    now = q.popleft()
    if now == 100:
        print(board[now])
        break
    for i in range(1, 7):
        next_i = now + i
        # 맵을 벗어나지 않고 아직 방문하지 않은 칸이라면
        if next_i <= 100 and not visited[next_i]:
            # 이동할 위치에 사다리가 있다면
            if next_i in ladder.keys():
                next_i = ladder[next_i]
            # 이동할 위치에 뱀이 있다면
            if next_i in snake.keys():
                next_i = snake[next_i]
            # 이동할 위치에 아무것도 없다면
            if not visited[next_i]:
                # 방문표시
                visited[next_i] = True
                q.append(next_i)
                board[next_i] = board[now] + 1
