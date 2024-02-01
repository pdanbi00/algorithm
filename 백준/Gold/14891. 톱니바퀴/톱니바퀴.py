# 아이디어 : 우선 회전 해야하는 톱니바퀴들을 다 조사함.
#           특정 톱니바퀴의 왼쪽에 있는 톱니바퀴들이 어느 방향으로 회전해야하는지
#           조사 다 하고나서 한개씩 회전시켜줌. 조사하면서 동시에 회전시키면 중간에 끼여있는건 2번 돌게 되고 이래서 안됨
# 0 : N극    1 : S극
n = 4
topnee = [list(map(int, input())) for _ in range(n)]
K = int(input()) # 회전 횟수

# 회전해야할 톱니바퀴 조사
for _ in range(K):
    no, dir = map(int, input().split())
    no -= 1
    d = [0] * n
    d[no] = dir
    # 왼쪽부터 조사
    for i in range(no-1, -1, -1):
        if topnee[i][2] == topnee[i+1][6]:
            break
        else:
            d[i] = -d[i+1]
    # 오른쪽 조사
    for i in range(no+1, n):
        if topnee[i-1][2] == topnee[i][6]:
            break
        else:
            d[i] = -d[i-1]
    # 회전시키기
    for i in range(n):
        if d[i] == 0:
            continue
        if d[i] == 1: # 시계방향
            temp = topnee[i][7]
            for j in range(7, 0, -1):
                topnee[i][j] = topnee[i][j-1]
            topnee[i][0] = temp
        elif d[i] == -1: # 반시계방향
            temp = topnee[i][0]
            for j in range(0, 7):
                topnee[i][j] = topnee[i][j+1]
            topnee[i][7] = temp
ans = 0
for i in range(n):
    if topnee[i][0] == 1:
        ans += (1 << i)
print(ans)