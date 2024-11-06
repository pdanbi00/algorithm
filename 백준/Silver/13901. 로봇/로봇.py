R, C = map(int, input().split())
k = int(input())
obstacle = []
for _ in range(k):
    br, bc = map(int, input().split())
    obstacle.append((br, bc))
rr, rc = map(int, input().split()) # 로봇 위치
directions = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dir = 0
visited = [[0] * C for _ in range(R)]
visited[rr][rc] = 1
board = [[0] * C for _ in range(R)]
for i in range(k):
    br, bc = obstacle[i][0], obstacle[i][1]
    board[br][bc] = 'X'

while True:
    possible = False
    for k in range(4):
        n_dir = (dir + k) % 4
        if directions[n_dir] == 1: # 상
            nr = rr + dr[0]
            nc = rc + dc[0]
        elif directions[n_dir] == 2: # 하
            nr = rr + dr[1]
            nc = rc + dc[1]
        elif directions[n_dir] == 3: # 좌
            nr = rr + dr[2]
            nc = rc + dc[2]
        elif directions[n_dir] == 4: # 우
            nr = rr + dr[3]
            nc = rc + dc[3]

        if 0 <= nr < R and 0 <= nc < C:
            if visited[nr][nc] == 0 and board[nr][nc] != 'X':
                visited[nr][nc] = 1
                rr = nr
                rc = nc
                dir = n_dir
                possible = True
                break

    if not possible:
        break
print(rr, rc)