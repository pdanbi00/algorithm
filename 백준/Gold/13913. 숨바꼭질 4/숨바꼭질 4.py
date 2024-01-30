from collections import deque
import sys
MAX = 200000
sys.setrecursionlimit(MAX)
checked = [False] * MAX
board = [-1] * MAX
via = [-1] * MAX

N, K = map(int, input().split())
checked[N] = True
board[N] = 0

q = deque()
q.append(N)
while q:
    now = q.popleft()
    if now-1 >= 0 and not checked[now-1]:
        q.append(now-1)
        checked[now-1] = True
        board[now-1]  = board[now] + 1
        via[now-1] = now
    if now+1 < MAX and not checked[now+1]:
        q.append(now+1)
        checked[now+1] = True
        board[now+1] = board[now] + 1
        via[now+1] = now
    if now*2 < MAX and not checked[now*2]:
        q.append(now*2)
        checked[now*2] = True
        board[now*2] = board[now] + 1
        via[now*2] = now
print(board[K])
def go(n, k):
    if n != k:
        go(n, via[k])
    print(k, end = ' ')
go(N, K)