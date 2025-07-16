N = int(input())
target = int(input())
board = [[0] * N for _ in range(N)]
cnt = 1
r = N // 2
c = N // 2
board[r][c] = 1
num = 2

while cnt <= N // 2:
    r -= 1
    if num == target:
        target_r = r+1
        target_c = c+1
    board[r][c] = num
    num += 1

    # 오른쪽으로 가면서 채우기
    tmp = 0
    while tmp < cnt * 2 - 1:
        c += 1
        if num == target:
            target_r = r+1
            target_c = c+1
        board[r][c] = num
        num += 1
        tmp += 1

    # 아래쪽으로 가면서 채우기
    tmp = 0
    while tmp < cnt * 2:
        r += 1
        if num == target:
            target_r = r+1
            target_c = c+1
        board[r][c] = num
        num += 1
        tmp += 1

    # 왼쪽으로 가면서 채우기
    tmp = 0
    while tmp < cnt * 2:
        c -= 1
        if num == target:
            target_r = r+1
            target_c = c+1
        board[r][c] = num
        num += 1
        tmp += 1

    # 위쪽으로 가면서 채우기
    tmp = 0
    while tmp < cnt * 2:
        r -= 1
        if num == target:
            target_r = r+1
            target_c = c+1
        board[r][c] = num
        num += 1
        tmp += 1

    cnt += 1
if target == 1:
    target_r = N // 2 + 1
    target_c = N // 2 + 1

for i in range(N):
    print(*board[i])

print(target_r, target_c)
'''
4 1 1 2 3
3 2 1 1 1
2 1 0 1 2
1 2 1 2 3
4 3 2 1 4
'''