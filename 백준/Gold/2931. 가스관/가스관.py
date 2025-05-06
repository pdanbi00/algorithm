# 가스관이 끊어진 지점을 먼저 찾고, 거기에 모든 가스관을 다 끼워보고 M에서 Z까지 갈 수 있는지 확인
from collections import deque

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

dirDict = {}
dirDict['|'] = {0 : 0, 2 : 2}
dirDict['-'] = {1 : 1, 3 : 3}
dirDict['+'] = {0 : 0, 2 : 2, 1 : 1, 3 : 3}
dirDict['1'] = {3 : 2, 0 : 1}
dirDict['2'] = {2 : 1, 3 : 0}
dirDict['3'] = {1 : 0, 2 : 3}
dirDict['4'] = {1 : 2, 0 : 3}

R, C = map(int, input().split())
board = []
m_r, m_c = 0, 0
z_r, z_c = 0, 0
visitedSet = set()
for i in range(R):
    arr = list(input())
    for j in range(C):
        if arr[j] != '.':
            visitedSet.add((i, j))

        if arr[j] == 'M':
            m_r, m_c = i, j
        elif arr[j] == 'Z':
            z_r, z_c = i, j
    board.append(arr)

def findLostPos(board, s_r, s_c):
    q = deque()
    d = -1
    for k in range(4):
        nr = s_r + dr[k]
        nc = s_c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] != '.' and board[nr][nc] != 'Z':
                d = k
                q.append((nr, nc))
                break

    while q:
        r, c = q.popleft()
        new_d = dirDict[board[r][c]][d]
        nr = r + dr[new_d]
        nc = c + dc[new_d]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == '.':
                return (nr, nc)
            else:
                d = new_d
                q.append((nr, nc))

def testRoute(board, s_r, s_c):
    visited = set()
    visited.add((s_r, s_c))
    q = deque()
    d = -1
    for k in range(4):
        nr = s_r + dr[k]
        nc = s_c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] != '.' and board[nr][nc] != 'Z':
                d = k
                q.append((nr, nc))
                visited.add((nr, nc))
                break
    while q:
        r, c = q.popleft()
        if d not in dirDict[board[r][c]]:
            return False
        new_d = dirDict[board[r][c]][d]
        nr = r + dr[new_d]
        nc = c + dc[new_d]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == '.':
                return False
            elif board[nr][nc] == 'Z':
                visited.add((nr, nc))
                if visited == visitedSet:
                    return True
                return False

            else:
                d = new_d
                q.append((nr, nc))
                visited.add((nr, nc))
    return False

lostPos = findLostPos(board, m_r, m_c)
visitedSet.add(lostPos)
for key in ('|', '-', '+', '1', '2', '3', '4'):
    board[lostPos[0]][lostPos[1]] = key
    if testRoute(board, m_r, m_c):
        print(lostPos[0]+1, lostPos[1]+1, key)
        break
    board[lostPos[0]][lostPos[1]] = '.'