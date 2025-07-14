from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
board = []
virus_dict = dict()
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] != 0:
            if arr[j] in virus_dict:
                virus_dict[arr[j]].append((i, j))
            else:
                virus_dict[arr[j]] = [(i, j)]
    board.append(arr)

S, X, Y = map(int, input().split())

time = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while time < S:
    q = deque()
    for i in range(1, K+1):
        if i in virus_dict:
            for r, c in virus_dict[i]:
                q.append((r, c, i))
            virus_dict[i] = []
    while q:
        r, c, num = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0:
                    board[nr][nc] = num
                    virus_dict[num].append((nr, nc))
    time += 1

print(board[X-1][Y-1])