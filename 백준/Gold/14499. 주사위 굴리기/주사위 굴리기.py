N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0] * 7
dx = [0, 0, -1, 1] # 행
dy = [1, -1, 0, 0] # 열
for command in commands:
    command -= 1
    nx = x + dx[command]
    ny = y + dy[command]
    if 0 <= nx < N and 0 <= ny < M:
        if command == 0: #동쪽으로 이동
            dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]

        elif command == 1: #서쪽으로 이동
            dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]

        elif command == 2: #북쪽으로 이동
            dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]

        elif command == 3: #남쪽으로 이동
            dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[6]
        else:
            dice[6] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(dice[1])
    else:
        continue