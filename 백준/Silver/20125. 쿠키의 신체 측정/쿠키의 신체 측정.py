N = int(input())
board = [input() for _ in range(N)]

find = False
# 머리 찾아서 심장 찾기
for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            heart = [i+1, j]
            find = True
            break
    if find:
        break
# print(heart)
# 왼팔 찾기
left_arm = 0
for i in range(heart[1] - 1, -1, -1):
    if board[heart[0]][i] == '*':
        left_arm += 1
    else:
        break

# 오른팔 찾기
right_arm = 0
for i in range(heart[1] + 1, N):
    if board[heart[0]][i] == '*':
        right_arm += 1
    else:
        break

# 허리 찾기
waist = 0
for i in range(heart[0]+1, N):
    if board[i][heart[1]] == '*':
        waist += 1
    else:
        waist_idx = [i-1, heart[1]]
        break

# 왼쪽 다리 찾기
left_leg = 0
for i in range(waist_idx[0]+1, N):
    if board[i][waist_idx[1]-1] == '*':
        left_leg += 1
    else:
        break
# 오른쪽 다리 찾기
right_leg = 0
for i in range(waist_idx[0]+1, N):
    if board[i][waist_idx[1]+1] == '*':
        right_leg += 1
    else:
        break

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)