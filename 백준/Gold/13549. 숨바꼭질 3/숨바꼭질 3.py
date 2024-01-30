from collections import deque
MAX = 200000
board = [-1] * (MAX+1)
N, K = map(int, input().split())
q = deque()
q.append(N)
board[N] = 0
while q:
    idx = q.popleft()
    if idx == K:
        print(board[idx])
        break
    if idx*2 <= MAX and board[idx*2] == -1:
        q.appendleft(idx*2)
        board[idx*2] = board[idx]
    if idx-1 >= 0 and board[idx-1] == -1:
        q.append(idx-1)
        board[idx-1] = board[idx] + 1
    if idx+1 <= MAX and board[idx+1] == -1:
        q.append(idx+1)
        board[idx+1] = board[idx] + 1