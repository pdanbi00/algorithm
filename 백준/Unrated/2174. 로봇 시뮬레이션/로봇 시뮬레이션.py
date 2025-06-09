A, B = map(int, input().split())
N, M = map(int, input().split())
board = [[-1] * A for _ in range(B)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
robot_dict = dict()

for i in range(N):
    c, r, d = input().split()
    r = int(r)
    c = int(c)
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    elif d == 'W':
        d = 3

    robot_dict[i+1] = [B-(r-1)-1, c-1, d]
    board[B-(r-1)-1][c-1] = i+1
# for i in range(B):
#     print(board[i])

possible = True
for _ in range(M):
    i, command, cnt = input().split()
    i = int(i)
    cnt = int(cnt)
    r, c, d = robot_dict[i]

    if command == 'L':
        d = (d + (3 * cnt)) % 4
        robot_dict[i] = [r, c, d]
    elif command == 'R':
        d = (d + (1 * cnt)) % 4
        robot_dict[i] = [r, c, d]
    elif command == 'F':
        while cnt > 0:
            cnt -= 1
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < B and 0 <= nc < A:
                if board[nr][nc] != -1:
                    print(f'Robot {i} crashes into robot {board[nr][nc]}')
                    possible = False
                    break
                else:
                    robot_dict[i] = [nr, nc, d]
                    board[r][c] = -1
                    board[nr][nc] = i
                    r = nr
                    c = nc
            else:
                print(f'Robot {i} crashes into the wall')
                possible = False
                break
    if not possible:
        break

if possible:
    print('OK')