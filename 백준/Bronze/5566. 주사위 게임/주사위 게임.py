N, M = map(int,input().split())

board = []
now = 0
for _ in range(N):
    n = int(input())
    board.append(n)
for i in range(M):
    move = int(input())
    now += move
    if now >= N-1:
        print(i+1)
        break
    now += board[now]
    if now >= N-1:
        print(i+1)
        break
