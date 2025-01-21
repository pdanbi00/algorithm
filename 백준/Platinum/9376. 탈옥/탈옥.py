# 1번 죄수 위치에서 탈출하기
# 2번 죄수 위치에서 탈출하기
# 상근이 위치에서 탈출하기

# 세 위치에서 각각 bfs를 돌림. 그럼 특정 위치까지 가기 위해서 문을 몇번 열어야하는지 알 수 있음
# 이것들을 다 더해주면 됨. 근데 이건 중복 제거 안한 상태.
# 1번 수감자가 연 문을 상근이도 열었을 수 있음.
# 즉, 특정 문을 여러번 열었는지에 대한 정보도 담아야 됨.
# 따라서 최소가 되는 위치의 값을 가져와야 됨. 여기서의 최소란 문을 중복해서 열지 않았다는 의미.
# 만약 가장 작은 숫자의 위치가 문이라면 -2해주기. 문의 위치에 저장된 값음 문을 열었다고 가정하기 때문에 -2 해서 3명 중 한명만 문 열었다고 계산

from collections import deque
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i, j):
    visited = [[-1] * (w+2) for _ in range(h+2)] # 열어야하는 문 개수

    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < (h+2) and 0 <= nc < (w+2):
                if visited[nr][nc] == -1:
                    if board[nr][nc] == '.' or board[nr][nc] == '$': # 문 안열고 간 경우
                        visited[nr][nc] = visited[r][c]
                        q.appendleft((nr, nc))
                    elif board[nr][nc] == '#':
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))

    return visited

for _ in range(T):
    h, w = map(int, input().split())

    # 상근이 위치를 특정하기 어렵기 때문에 board 상하좌우에 빈칸 추가
    board = [list('.' * (w+2))] # 맨 윗줄 추가
    for i in range(h):
        board.append(list('.' + input() + '.'))
    board.append(list('.' * (w+2)))

    prisoner = []
    for i in range(h+2):
        for j in range(w+2):
            if board[i][j] == '$':
                prisoner.append((i, j))

    first = bfs(prisoner[0][0], prisoner[0][1])
    second = bfs(prisoner[1][0], prisoner[1][1])
    sanggeun = bfs(0, 0)

    answer = 1e9

    for i in range(h+2):
        for j in range(w+2):
            # 상근이는 감옥 밖에서 접근하고 나머지 죄수들은 감옥 안에서 접근하기 때문에
            # 이 세명이 만나는 곳이면? 상근이가 데리고 밖으로 갈 수 있다는 의미임
            if first[i][j] != -1 and second[i][j] != -1 and sanggeun[i][j] != -1:
                result = first[i][j] + second[i][j] + sanggeun[i][j] # 해당 위치에서 문 연 개수

                if board[i][j] == '*': # 벽은 제외하기
                    continue

                if board[i][j] == '#': # 한명만 열어도 되니깐 나머지 사람이 연 갯수인 2 빼줌
                    result -= 2
                answer = min(answer, result)

    print(answer)
