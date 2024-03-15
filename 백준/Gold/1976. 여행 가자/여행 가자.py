# bfs
from collections import deque
N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
graph = [set() for _ in range(N)]
route = list(map(int, input().split()))


def bfs(i, j):
    visitied = [0] * N
    q = deque()
    q.append(j)
    graph[i].add(j)
    visitied[j] = 1
    while q:
        idx = q.popleft()
        for k in range(N):
            if board[idx][k] == 1 and visitied[k] == 0:
                q.append(k)
                graph[i].add(k)
                visitied[k] = 1

for i in range(N):
    for j in range(N):
        if i == j :
            board[i][j] = 1
        if board[i][j] == 1:
           bfs(i, j)
if N == 0:
    possible = False

else:
    possible = True
    for i in range(0, len(route)-1):
        if route[i+1]-1 not in graph[route[i]-1]:
            possible = False
            break
if possible:
    print("YES")
else:
    print("NO")
