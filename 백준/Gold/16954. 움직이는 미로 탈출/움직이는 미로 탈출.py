from collections import deque

board = []
walls = []# 벽인 곳들의 정보를 담음

for i in range(8):
    arr = list(input())
    for j in range(8):
        if arr[j] == '#':
            walls.append((i, j))
    board.append(arr)

dr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

time = 0 # 시간. 9초 이상이면 벽 다 사라지니깐 무조건 도달 가능
q = deque()
q.append((7, 0)) # 행, 열
while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        if (r, c) in walls:
            continue

        if r == 0 or time == 9:
            print(1)
            exit()
        # 캐릭터 이동하기
        for k in range(9):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 8 and 0 <= nc < 8:
                if (nr, nc) not in walls:
                    q.append((nr, nc))
    for i in range(len(walls)):
        walls[i] = (walls[i][0] + 1, walls[i][1])
    time += 1
print(0)