# 학생 번호 한 개 받고, 각 칸마다 인접 4 방향에 좋아하는 학생 번호 몇개 있는지, 비어있는 칸 몇개 있는지 확인
# 최대값이랑 비교하면서 최대값이랑 같거나 큰거만 남겨둠
# 개수 다 찾고 나서 정렬해서 위치 정해주기

N = int(input())
board = [[0] * N for _ in range(N)]
likes_info = {}
seat_info = {}
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 자리 정하기
for _ in range(N**2):
    s, *likes = map(int, input().split())
    likes_info[s] = likes
    like_info = {}
    sort_arr = []
    max_like_cnt = 0
    # 모든 칸을 살펴보면서 각 칸의 상하좌우에 좋아하는 학생 번호가 있는지 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                ci, cj = i, j
                cnt = 0
                for d in range(4):
                    nr, nc = i + dr[d], j + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] in likes: # 근처에 좋아하는 학생이 있으면
                            cnt += 1
                            if (i, j) not in like_info:
                                like_info[(i, j)] = [1, 0]
                            else:
                                like_info[(i, j)][0] += 1
                        if board[nr][nc] == 0:
                            if (i, j) not in like_info:
                                like_info[(i, j)] = [0, 1]
                            else:
                                like_info[(i, j)][1] += 1
                if cnt > max_like_cnt:
                    max_like_cnt = cnt
    if len(like_info) == 0:
        find_zero = False
        for ni in range(N):
            for nj in range(N):
                if board[ni][nj] == 0:
                    board[ni][nj] = s
                    find_zero = True
                    break
            if find_zero:
                break

    elif len(like_info) > 0:
        for k, v in like_info.items():
            if v[0] == max_like_cnt:
                sort_arr.append((k, v[1]))
        sort_arr.sort(key=lambda x : (x[1], -x[0][0], -x[0][1]), reverse=True)
        board[sort_arr[0][0][0]][sort_arr[0][0][1]] = s
    # print(board)
ans = 0
# 만족도 구하기
for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):
            nr, nc = i + dr[d], j + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] in likes_info[board[i][j]]:
                    cnt += 1
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)

'''
3
7 9 3 8 2 
5 7 3 8 6
3 5 2 4 9
9 6 8 3 4
8 5 3 1 6
6 3 8 5 4
2 6 4 8 7
1 8 3 4 5
4 7 9 3 8
'''