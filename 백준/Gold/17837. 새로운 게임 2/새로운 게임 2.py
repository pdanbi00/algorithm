N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

pieces = [[[] for _ in range(N)] for _ in range(N)]
piecesDict = dict()
for i in range(1, K+1):
    r, c, d = map(int, input().split())
    pieces[r-1][c-1].append(i)
    piecesDict[i] = [r-1, c-1, d]

def game():
    global end
    over = False
    dr = [0, 0, 0, -1, 1]
    dc = [0, 1, -1, 0, 0]

    for i in range(1, K+1):
        r, c, d = piecesDict[i]
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nr < N and 0 <= nc < N):
            if board[nr][nc] == 0: # 이동할 칸이 흰색일 경우
                tmp = []
                while pieces[r][c]:
                    now = pieces[r][c].pop()
                    tmp.append(now)
                    if now == i:
                        break
                while tmp:
                    num = tmp.pop()
                    # pieces에 새로운 말 추가
                    pieces[nr][nc].append(num)
                    if len(pieces[nr][nc]) >= 4:
                        over = True
                        end = True
                        break
                    cur = piecesDict[num]
                    # piecesDict에서 말 정보 업데이트
                    piecesDict[num] = [nr, nc, cur[2]]

                if over:
                    break

            elif board[nr][nc] == 1: # 빨간 색일 경우 순서 바꿔서 추가하기
                while pieces[r][c]:
                    now = pieces[r][c].pop()
                    # pieces에 새로운 말 추가
                    pieces[nr][nc].append(now)
                    if len(pieces[nr][nc]) >= 4:
                        over = True
                        end = True
                        break
                    cur = piecesDict[now]

                    # piecesDict에서 말 정보 업데이트
                    piecesDict[now] = [nr, nc, cur[2]]
                    if now == i:
                        break
                if over:
                    break
            elif board[nr][nc] == 2:
                if d == 1:
                    nr = r + dr[2]
                    nc = c + dc[2]
                    d = 2
                elif d == 2:
                    nr = r + dr[1]
                    nc = c + dc[1]
                    d = 1
                elif d == 3:
                    nr = r + dr[4]
                    nc = c + dc[4]
                    d = 4
                elif d == 4:
                    nr = r + dr[3]
                    nc = c + dc[3]
                    d = 3

                if (0 <= nr < N and 0 <= nc < N):
                    if board[nr][nc] == 0:  # 이동할 칸이 흰색일 경우
                        tmp = []
                        while pieces[r][c]:
                            now = pieces[r][c].pop()
                            tmp.append(now)
                            if now == i:
                                break
                        while tmp:
                            num = tmp.pop()
                            # pieces에 새로운 말 추가
                            pieces[nr][nc].append(num)
                            if len(pieces[nr][nc]) >= 4:
                                over = True
                                end = True
                                break
                            cur = piecesDict[num]
                            # piecesDict에서 말 정보 업데이트
                            if num == i:
                                # 바뀐 방향으로 업데이트
                                piecesDict[num] = [nr, nc, d]
                            else:
                                piecesDict[num] = [nr, nc, cur[2]]

                        if over:
                            break

                    elif board[nr][nc] == 1:  # 빨간 색일 경우 순서 바꿔서 추가하기
                        while pieces[r][c]:
                            now = pieces[r][c].pop()
                            # pieces에 새로운 말 추가
                            pieces[nr][nc].append(now)
                            if len(pieces[nr][nc]) >= 4:
                                over = True
                                end = True
                                break
                            cur = piecesDict[now]

                            # piecesDict에서 말 정보 업데이트
                            if now == i:
                                # 바뀐 방향으로 업데이트
                                piecesDict[now] = [nr, nc, d]
                                break
                            else:
                                piecesDict[now] = [nr, nc, cur[2]]

                        if over:
                            break
                    elif board[nr][nc] == 2:
                        # piecesDict에서 현재 말 방향만 업데이트
                        piecesDict[i] = [r, c, d]

        else: # 범위 넘어간 경우
            if d == 1:
                nr = r + dr[2]
                nc = c + dc[2]
                d = 2
            elif d == 2:
                nr = r + dr[1]
                nc = c + dc[1]
                d = 1
            elif d == 3:
                nr = r + dr[4]
                nc = c + dc[4]
                d = 4
            elif d == 4:
                nr = r + dr[3]
                nc = c + dc[3]
                d = 3

            if (0 <= nr < N and 0 <= nc < N):
                if board[nr][nc] == 0:  # 이동할 칸이 흰색일 경우
                    tmp = []
                    while pieces[r][c]:
                        now = pieces[r][c].pop()
                        tmp.append(now)
                        if now == i:
                            break
                    while tmp:
                        num = tmp.pop()
                        # pieces에 새로운 말 추가
                        pieces[nr][nc].append(num)
                        if len(pieces[nr][nc]) >= 4:
                            over = True
                            end = True
                            break
                        cur = piecesDict[num]
                        # piecesDict에서 말 정보 업데이트
                        if num == i:
                            # 바뀐 방향으로 업데이트
                            piecesDict[num] = [nr, nc, d]
                        else:
                            piecesDict[num] = [nr, nc, cur[2]]

                    if over:
                        break

                elif board[nr][nc] == 1:  # 빨간 색일 경우 순서 바꿔서 추가하기
                    while pieces[r][c]:
                        now = pieces[r][c].pop()
                        # pieces에 새로운 말 추가
                        pieces[nr][nc].append(now)
                        if len(pieces[nr][nc]) >= 4:
                            over = True
                            end = True
                            break
                        cur = piecesDict[now]

                        # piecesDict에서 말 정보 업데이트
                        if now == i:
                            # 바뀐 방향으로 업데이트
                            piecesDict[now] = [nr, nc, d]
                            break
                        else:
                            piecesDict[now] = [nr, nc, cur[2]]

                    if over:
                        break
                elif board[nr][nc] == 2:
                    # piecesDict에서 현재 말 방향만 업데이트
                    piecesDict[i] = [r, c, d]

end = False
answer = 1
while answer <= 1000:
    game()
    if end:
        break
    answer += 1
if end:
    print(answer)
else:
    print(-1)

