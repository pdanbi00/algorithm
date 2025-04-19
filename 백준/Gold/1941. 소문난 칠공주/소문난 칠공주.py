from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(arr):
    visited = [[1] * 5 for _ in range(5)]
    for i in arr:
        visited[i[0]][i[1]] = 0
    q = deque()
    q.append(arr[0])
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 5 and 0 <= nc < 5:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    check += 1
                    q.append((nr, nc))
    if check != 7:
        return False
    return True

def dfs(depth, start, count):
    global result
    # 임도연 파가 4명 이상이면 중단
    if count >= 4:
        return
    if depth == 7:
        if bfs(A):
            result += 1
        return

    for i in range(start, 25):
        r = i // 5
        c = i % 5
        A.append((r, c))
        if board[r][c] == 'Y':
            dfs(depth+1, i+1, count + 1)
        else:
            dfs(depth+1, i+1, count)
        A.pop()

board = [list(input()) for _ in range(5)]
A = []
result = 0
dfs(0, 0, 0)
print(result)