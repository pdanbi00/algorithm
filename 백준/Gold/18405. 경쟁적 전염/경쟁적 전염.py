from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
board = []
heap = []

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] != 0:
            heappush(heap, (arr[j], i, j))
    board.append(arr)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

S, X, Y = map(int, input().split())

for _ in range(S):
    next_virus = []
    while heap:
        now = heappop(heap)
        n, r, c = now[0], now[1], now[2]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0:
                    board[nr][nc] = n
                    next_virus.append((n, nr, nc))

    for vir in next_virus:
        heappush(heap, vir)

print(board[X-1][Y-1])