from collections import deque
MAX = 200000

N, K = map(int, input().split())
board = [[-1, -1] for _ in range(MAX+1)]
checked = [False] * (MAX+1)
ans = []
q = deque()
q.append(N)
board[N][0] = 0
checked[N] = True
while q:
    idx = q.popleft()
    if idx == K:
        print(board[K][0])
        ans.append(idx)
        while True:
            if board[idx][1] == -1:
                break
            ans.append(board[idx][1])
            idx = board[idx][1]
        break
    for n_idx in [idx-1, idx+1, idx*2]:
        if 0 <= n_idx <= MAX and checked[n_idx] == False:
            q.append(n_idx)
            checked[n_idx] = True
            board[n_idx][0] = board[idx][0] + 1
            board[n_idx][1] = idx
ans.reverse()
for i in ans:
    print(i, end=' ')
