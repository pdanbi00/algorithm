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
    able_position = [] # 현재 학생이 앉을 수 있는 자리 후보
    likes_info[s] = likes

    # 모든 칸을 살펴보면서 각 칸의 상하좌우에 좋아하는 학생 번호가 있는지 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                like = 0 # board[i][j] 주변에 좋아하는 친구 수
                blank = 0 # board[i][j] 주변 빈자리 수
                for d in range(4):
                    nr, nc = i + dr[d], j + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        # 근처에 좋아하는 학생이 있으면
                        if board[nr][nc] in likes:
                            like += 1
                        # 근처에 빈자리가 있으면
                        if board[nr][nc] == 0:
                            blank += 1
                able_position.append([like, blank, i, j])
    # 현재 학생이 앉을 수 있는 자리를 like, blank는 내림차순, i, j는 오름차순으로 정렬
    able_position.sort(key=lambda x : (x[0], x[1], -x[2], -x[3]), reverse=True)

    # 조건 우선순위가 제일 높은 위치에 학생 자리 지정
    board[able_position[0][2]][able_position[0][3]] = s

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