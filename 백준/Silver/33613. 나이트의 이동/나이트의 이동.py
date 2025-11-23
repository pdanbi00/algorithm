from collections import deque
N = int(input())
R, C = map(int, input().split())
R -= 1
C -= 1

if N > 3:
    if N % 2 == 0:
        print((N * N) // 2)
    else:
        if R % 2 == C % 2:
            print((N * N) // 2 + 1)
        else:
            print((N * N) // 2)

else:
    board = [[False] * N for _ in range(N)]
    board[R][C] = True
    answer = 1

    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]

    q = deque()
    q.append((R, C))

    while q:
        r, c = q.popleft()

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                for k2 in range(8):
                    nnr = nr + dr[k2]
                    nnc = nc + dc[k2]
                    if 0 <= nnr < N and 0 <= nnc < N:
                        if not board[nnr][nnc]:
                            q.append((nnr, nnc))
                            answer += 1
                            board[nnr][nnc] = True

    print(answer)