from collections import deque
N, M = map(int, input().split())
board = [list(input()) for _ in range(3)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = []

q = deque()
q.append([(0, 0)])
q.append([(0, 2)])
q.append([(1, 1)])
q.append([(2, 0)])
q.append([(2, 2)])

while q:
    now = q.popleft()
    # print(now)
    if len(now) == M * 2 - 1:
        tmp = int(board[now[0][0]][now[0][1]])
        for i in range(1, len(now), 2):
            # print(i)
            if board[now[i][0]][now[i][1]] == '-':
                tmp -= int(board[now[i+1][0]][now[i+1][1]])
            elif board[now[i][0]][now[i][1]] == '+':
                tmp += int(board[now[i+1][0]][now[i+1][1]])
        # print(tmp)
        if tmp == N:
            answer = now
            break

    else:
        r, c = now[-1][0], now[-1][1]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < 3 and 0 <= nc < 3:
                if (nr, nc) not in now:
                    q.append(now + [(nr, nc)])

if answer:
    print(1)
    for i in range(2 * M - 1):
        print(answer[i][0], answer[i][1])
else:
    print(0)