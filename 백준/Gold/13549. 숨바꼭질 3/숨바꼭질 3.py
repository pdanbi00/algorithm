from collections import deque
MAX = 200000
N, K = map(int, input().split())
board = [-1] * (MAX+1)
q = deque()
next_q = deque()
q.append(N)
board[N] = 0
while q:
    idx = q.popleft()
    if idx == K:
        print(board[idx])
        break
    if idx*2 <= MAX and board[idx*2] == -1:
        q.append(idx*2)
        board[idx*2] = board[idx]
    # 순서가 - 1이 + 1 보다 먼저 와야 됨. 4에서 6 가는 경우 생각 해보면 됨.
    if idx - 1 >= 0 and board[idx - 1] == -1:
        next_q.append(idx - 1)
        board[idx - 1] = board[idx] + 1
    if idx + 1 <= MAX and board[idx+1] == -1:
        next_q.append(idx+1)
        board[idx+1] = board[idx] + 1

    # q가 비게 되면 첫번째 큐는 다 사용한거니깐 두번째 큐를 첫번째 큐로 만들어주고 새로운 큐를 두번째 큐로 만들기
    if not q:
        q = next_q
        next_q = deque()