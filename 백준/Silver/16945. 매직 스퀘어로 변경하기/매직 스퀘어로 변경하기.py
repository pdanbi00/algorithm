from itertools import permutations
board = [list(map(int, input().split())) for _ in range(3)]

arr = [i for i in range(1, 10)]

ans = 1e9

for perm in permutations(arr, 9):
    new_arr = [[0] * 3 for _ in range(3)]
    idx = 0
    for i in range(3):
        for j in range(3):
            new_arr[i][j] = perm[idx]
            idx += 1
    possible = True
    # 각 행 확인
    tmp = sum(new_arr[0])
    for i in range(1, 3):
        if tmp != sum(new_arr[i]):
            possible = False
            break
    # 각 열 확인
    if possible:
        for i in range(3):
            total = 0
            for j in range(3):
                total += new_arr[j][i]
            if total != tmp:
                possible = False
                break

    # 대각선 확인
    if possible:
        total1 = new_arr[0][0] + new_arr[1][1] + new_arr[2][2]
        if total1 != tmp:
            possible = False

        if possible:
            total2 = new_arr[0][2] + new_arr[1][1] + new_arr[2][0]
            if total2 != tmp:
                possible = False

    if possible:
        total = 0
        for i in range(3):
            for j in range(3):
                total += abs(board[i][j] - new_arr[i][j])
        ans = min(total, ans)

print(ans)