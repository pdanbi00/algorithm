from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = []
tong = []
target = []
for i in range(N):
    arr = list(input().rstrip())
    for j in range(N):
        if arr[j] == 'B':
            tong.append((i, j))
        elif arr[j] == 'E':
            target.append((i, j))
    board.append(arr)

# 통나무 방향 판단하기
if tong[0][0] == tong[1][0]: # 가로
    start_d = 0
else: # 세로
    start_d = 1

# 통나무가 가로일 경우
def garo(tree, d, cnt):
    global q, visited

    # 상
    possible = True
    for r, c in tree:
        if not (0 <= r - 1 < N)  or board[r - 1][c] == '1':
            possible = False
            break
    if possible:
        t = tuple([(r-1, c) for r, c in tree])
        if t not in visited:
            q.append((t, d, cnt+1))
            visited.add(t)

    # 하
    possible = True
    for r, c in tree:
        if not (0 <= r + 1 < N) or board[r + 1][c] == '1':
            possible = False
            break
    if possible:
        t = tuple([(r + 1, c) for r, c in tree])
        if t not in visited:
            q.append((t, d, cnt + 1))
            visited.add(t)

    # 좌
    r, c = tree[0]
    if 0 <= c-1 < N and board[r][c-1] != '1':
        t = []
        for r, c in tree:
            t.append((r, c-1))
        t = tuple(t)
        if t not in visited:
            q.append((t, d, cnt+1))
            visited.add(t)
    # 우
    r, c = tree[2]
    if 0 <= c + 1 < N and board[r][c + 1] != '1':
        t = []
        for r, c in tree:
            t.append((r, c + 1))
        t = tuple(t)
        if t not in visited:
            q.append((t, d, cnt + 1))
            visited.add(t)
    # 회전
    possible = True
    for r, c in tree:
        if not (1 <= r < N-1):
            possible = False
            break
        if board[r-1][c] == '1' or board[r+1][c] == '1':
            possible = False
            break
    if possible:
        cr, cc = tree[1]
        t = tuple([(cr-1, cc), (cr, cc), (cr+1, cc)])
        if t not in visited:
            q.append((t, 1, cnt+1))
            visited.add(t)

# 통나무가 세로일 경우
def sero(tree, d, cnt):
    global q, visited
    # 상
    r, c = tree[0]
    if 0 <= r - 1 < N and board[r-1][c] != '1':
        t = []
        for r, c in tree:
            t.append((r-1, c))
        t = tuple(t)
        if t not in visited:
            q.append((t, d, cnt + 1))
            visited.add(t)

    # 하
    r, c = tree[2]
    if 0 <= r + 1 < N and board[r + 1][c] != '1':
        t = []
        for r, c in tree:
            t.append((r + 1, c))
        t = tuple(t)
        if t not in visited:
            q.append((t, d, cnt + 1))
            visited.add(t)

    # 좌
    possible = True
    for r, c in tree:
        if not (0 <= c - 1 < N) or board[r][c - 1] == '1':
            possible = False
            break
    if possible:
        t = tuple([(r, c - 1) for r, c in tree])
        if t not in visited:
            q.append((t, d, cnt + 1))
            visited.add(t)

    # 우
    possible = True
    for r, c in tree:
        if not (0 <= c + 1 < N) or board[r][c + 1] == '1':
            possible = False
            break
    if possible:
        t = tuple([(r, c + 1) for r, c in tree])
        if t not in visited:
            q.append((t, d, cnt + 1))
            visited.add(t)

    # 회전
    possible = True
    for r, c in tree:
        if not (1 <= c < N - 1):
            possible = False
            break
        if board[r][c - 1] == '1' or board[r][c + 1] == '1':
            possible = False
            break
    if possible:
        cr, cc = tree[1]
        t = tuple([(cr, cc - 1), (cr, cc), (cr, cc + 1)])
        if t not in visited:
            q.append((t, 0, cnt + 1))
            visited.add(t)

answer = 1e9
target = tuple(target)
visited = set()
q = deque()
q.append((tong, start_d, 0)) # [나무 위치들, 방향, 움직인 횟수]
visited.add(tuple(tong))
while q:
    tree, d, cnt = q.popleft()
    # print(tree)
    if tree == target:
        answer = cnt
        break
    if d == 0:
        garo(tree, d, cnt)
    else:
        sero(tree, d, cnt)

if answer == 1e9:
    print(0)
else:
    print(answer)