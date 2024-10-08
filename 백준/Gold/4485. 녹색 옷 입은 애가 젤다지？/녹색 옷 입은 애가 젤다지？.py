# 다익스트라
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    q = []
    heappush(q, (board[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, r, c = heappop(q)

        if r == N-1 and c == N-1:
            print(f'Problem {tc}: {distance[r][c]}')
            return
        for p in range(4):
            nr = r + dr[p]
            nc = c + dc[p]

            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + board[nr][nc]

                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost
                    heappush(q, (distance[nr][nc], nr, nc))
tc = 1
while True:

    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e9] * N for _ in range(N)]
    dijkstra()
    tc += 1