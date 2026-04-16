from collections import deque
H, W = map(int, input().split())
board = []
for i in range(H):
    arr = list(input())
    for j in range(W):
        if arr[j] == 'D':
            s_r, s_c = i, j
        elif arr[j] == 'Z':
            e_r, e_c = i, j
    board.append(arr)

N = int(input())
disturbance = [list(input().split()) for _ in range(N)]

dr = {'W' : -1, 'A' : 0, 'S' : 1, 'D' : 0}
dc = {'W' : 0, 'A' : -1, 'S' : 0, 'D' : 1}

q = deque()
visited = set()

q.append((s_r, s_c, 0, '')) # r, c, idx, path

possible = False
while q:
    r, c, idx, path = q.popleft()


    if r == e_r and c == e_c and idx <= N:
        possible = True
        answer = path
        break

    if idx >= N:
        continue

    for k in range(2):
        d = disturbance[idx][k]
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < H and 0 <= nc < W:
            if board[nr][nc] != '@' and idx + 1 <= N and (path + d) not in visited:
                q.append((nr, nc, idx+1, path+d))
                visited.add(path+d)
if possible:
    print("YES")
    print(answer)
else:
    print("NO")