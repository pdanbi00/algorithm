N, M, H = map(int, input().split())
sadari = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    sadari[a-1][b-1] = 1

# 1자로 내려가는지 확인하기
# 가로선 개수 0개부터 3개까지 생성하고 straight 함수 실행 완탐
def straight(): # 1자로 내려가는지 확인하는 함수. 1자로 내려가면 True, 아니면 False
    for i in range(N): # 시작할 사다리 번호
        start_num = i
        for j in range(H):
            # 오른쪽으로 이동
            if sadari[j][start_num] == 1:
                start_num += 1
            elif sadari[j][start_num-1] == 1 and start_num > 0:
                start_num -= 1
        if start_num != i:
            return False
    return True

# 가로선 추가하면서 확인하는 함수 dfs
def dfs(cnt, r, c):
    global answer
    if answer <= cnt:
        return
    if straight():
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return
    for i in range(r, H):
        for j in range(N-1):
            if sadari[i][j] == 0:
                sadari[i][j] = 1
                dfs(cnt+1, i, j+2) # 연속된 가로선을 만들지 않기 위해 j+2
                sadari[i][j] = 0

answer = 4
dfs(0, 0, 0)
if answer > 3:
    answer = -1
print(answer)