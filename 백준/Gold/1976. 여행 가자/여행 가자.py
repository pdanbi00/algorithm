# bfs
from collections import deque
N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
route = list(map(int, input().split()))


def bfs(start, end):
    visitied = [0] * N
    q = deque()
    q.append(start)
    visitied[start] = 1
    while q:
        idx = q.popleft()
        if idx == end:
            return True

        for k in range(N):
            if board[idx][k] == 1 and visitied[k] == 0:
                q.append(k)
                visitied[k] = 1
    # 다음 여행지로 못가는 경우
    return False

ans = "YES"
for i in range(M-1):
    possible = bfs(route[i]-1, route[i+1]-1)
    if not possible:
        ans = "NO"
        break
print(ans)

