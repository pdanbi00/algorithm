from itertools import combinations

N = int(input())
board = []
empty = []
teacher = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    arr = list(input().split())
    for j in range(N):
        if arr[j] == 'X':
            empty.append((i, j))
        elif arr[j] == 'T':
            teacher.append((i, j))
    board.append(arr)

def check():
    for t_r, t_c in teacher:
        for k in range(4):
            nr = t_r
            nc = t_c
            while True:
                nr += dr[k]
                nc += dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == 'S':
                        return False
                    elif board[nr][nc] == 'O':
                        break
                else:
                    break
    return True
possible = False
for com in combinations(empty, 3):
    for c in com:
        board[c[0]][c[1]] = 'O'
    if check():
        possible = True
        break
    for c in com:
        board[c[0]][c[1]] = 'X'
if possible:
    print("YES")
else:
    print("NO")