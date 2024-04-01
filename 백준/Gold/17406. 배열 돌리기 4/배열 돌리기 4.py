# 순열로 회전 순서 정하고 각각 다 돌아가면서 ㄱㄱ

'''
시계 방향 회전은 회전하는 숫자들끼리 한 그룹으로 묶어서
각 그룹 안에서 회전 시키고 다시 넣어주면 됨.
'''
from itertools import permutations
import sys
input = sys.stdin.readline

def rotate(r_s, c_s, r_e, c_e):
    arrs = []
    for k in range((r_e - r_s) // 2): # 돌리는 횟수, 제일 바깥 테두리, 그 안 테두리 ... 총 (마무리 행 - 시작행) // 2임. 왜냐면 무조건 홀수 행만큼 도니깐. 아 근데 중간 행은 안돌듯?
        arr = []
        # 제일 윗 행 넣기
        for j in range(k + c_s, c_e-k):
            arr.append(board[k+r_s][j])
        # 제일 오른쪽 열 넣기
        for i in range(r_s+k, r_e-k):
            arr.append(board[i][c_e-k])
        # 제일 아래 행 넣기
        for j in range(c_e-k, c_s + k, -1):
            arr.append(board[r_e-k][j])
        # 제일 왼쪽 열 넣기
        for i in range(r_e - k, r_s + k, -1):
            arr.append(board[i][c_s+k])
        arrs.append(arr)

    # 실제 회전 시키기. 회전 시키고 넣을 때는 위에꺼랑 순서 똑같아야 됨.
    for k in range((r_e - r_s) // 2):
        group = arrs[k]
        l = len(group)
        index = l-1
        # 제일 윗 행
        for j in range(k + c_s, c_e-k):
            board[r_s+k][j] = group[index]
            index = (index+1) % l
        # 제일 오른쪽 열
        for i in range(r_s+k, r_e-k):
            board[i][c_e-k] = group[index]
            index = (index+1) % l
        # 제일 아래 행
        for j in range(c_e-k, c_s + k, -1):
            board[r_e-k][j] = group[index]
            index = (index + 1) % l
        # 제일 왼쪽 열
        for i in range(r_e - k, r_s + k, -1):
            board[i][c_s + k] = group[index]
            index = (index + 1) % l

N, M, K = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(N)]
change = []
ans = 1e9
for i in range(K):
    a, b, c = map(int, input().split())
    change.append((a-1, b-1, c))
for perm in permutations(change, K):
    board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            board[i][j] = original[i][j]
    for p in perm:
        rotate(p[0]-p[2], p[1]-p[2], p[0]+p[2], p[1]+p[2])
    temp = sum(board[0])
    for i in range(1, N):
        temp = min(temp, sum(board[i]))
    ans = min(ans, temp)
print(ans)

