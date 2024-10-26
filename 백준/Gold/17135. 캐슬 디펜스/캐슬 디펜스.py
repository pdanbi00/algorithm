# board = M열, N+1행
# 궁수는 3명. N+1 행에 위치
# 적은 거리가 D 이하인 적 중에 가장 가까운 적, 거리가 같으면 가장 왼쪽에 있는 적
# 공격받으면 적은 제거됨. 공격 이후 적은 한칸씩 아래로 이동#
# 이동해서 N+1로 오게 되면 제거됨
from copy import deepcopy

N, M, D = map(int, input().split())
board = []
juck = 0 # 적의 수. while 문 break 조건이 될거임.
for _ in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 1:
            juck += 1
    board.append(arr)

def attack(i, j, k, new_board):
    global cnt
    global tong
    while cnt + tong < juck:
        gung1 = []
        gung2 = []
        gung3 = []
        # 공격 대상 찾기
        for r in range(N):
            for c in range(M):
                if new_board[r][c] == 1:
                    dis1 = abs(r - N) + abs(c - i)
                    dis2 = abs(r - N) + abs(c - j)
                    dis3 = abs(r - N) + abs(c - k)
                    if dis1 <= D:
                        gung1.append((dis1, r, c))
                    if dis2 <= D:
                        gung2.append((dis2, r, c))
                    if dis3 <= D:
                        gung3.append((dis3, r, c))
        if len(gung1) >= 1:
            gung1.sort(key=lambda x : (x[0], x[2]))
            # 공격
            new_board[gung1[0][1]][gung1[0][2]] = 0
            cnt += 1
        if len(gung2) >= 1:
            gung2.sort(key=lambda x: (x[0], x[2]))
            if new_board[gung2[0][1]][gung2[0][2]] == 1:
                # 공격
                new_board[gung2[0][1]][gung2[0][2]] = 0
                cnt += 1
        if len(gung3) >= 1:
            gung3.sort(key=lambda x: (x[0], x[2]))
            if new_board[gung3[0][1]][gung3[0][2]] == 1:
                # 공격
                new_board[gung3[0][1]][gung3[0][2]] = 0
                cnt += 1

        # 공격 이후 적들은 아래로 이동
        # N-1행에 남아있는 적들은 제거시키기
        for c in range(M):
            if new_board[N-1][c] == 1:
                tong += 1
                new_board[N-1][c] = 0

        # 나머지 적들은 아래로 한칸씩 이동
        for r in range(N-2, -1, -1):
            for c in range(M):
                new_board[r+1][c] = new_board[r][c]
        # 0 행은 0으로 다 채우기
        for c in range(M):
            new_board[0][c] = 0
    return cnt

ans = -1
for i in range(M-2): # 궁수 1 위치
    for j in range(i+1, M-1): # 궁수 2 위치
        for k in range(j+1, M): # 궁수 3 위치
            new_board = deepcopy(board)
            cnt = 0 # 공격 당해서 제거된 적의 수
            tong = 0 # 성에 도착해서 제거된 적의 수
            tmp = attack(i, j, k, new_board)
            ans = max(ans, tmp)
print(ans)