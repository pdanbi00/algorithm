T = int(input())
topnee = [list(map(int, input())) for _ in range(T)]
K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())
    num -= 1
    change = [0] * T
    change[num] = dir
    # 왼쪽부터 점검
    for i in range(num-1, -1, -1):
        if topnee[i][2] == topnee[i+1][6]:
            break
        else:
            change[i] = -change[i+1]
    # 오른쪽부터 점검
    for i in range(num + 1, T):
        if topnee[i][6] == topnee[i - 1][2]:
            break
        else:
            change[i] = -change[i - 1]

    # 회전시키기
    for i in range(T):
        if change[i] == 1: # 시계 방향 회전
            temp = topnee[i][7]
            for j in range(7, 0, -1):
                topnee[i][j] = topnee[i][j-1]
            topnee[i][0] = temp
        elif change[i] == -1: # 반시계 방향 회전
            temp = topnee[i][0]
            for j in range(0, 7):
                topnee[i][j] = topnee[i][j+1]
            topnee[i][7] = temp
ans = 0
for i in range(T):
    if topnee[i][0] == 1:
        ans += 1
print(ans)

