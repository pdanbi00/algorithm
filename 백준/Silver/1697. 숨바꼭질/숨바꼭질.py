from collections import deque
MAX = 200000

N, K = map(int, input().split())

board = [-1] * (MAX+1)
checked = [False] * (MAX+1)

q = deque()
q.append(N)
board[N] = 0
checked[N] = True
while q:
    idx = q.popleft()
    if idx == K:
        print(board[idx])
        break
    for n_idx in (idx-1, idx+1, idx*2):
        if 0 <= n_idx <= MAX and checked[n_idx] == False:
            q.append(n_idx)
            checked[n_idx] = True
            board[n_idx] = board[idx] + 1