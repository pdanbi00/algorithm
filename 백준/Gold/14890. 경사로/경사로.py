# 아이디어 : 각 행, 각 열을 1차원 배열로 만들어서 각각 확인한다.
#           옆에 칸이랑 값이 다르면 차이가 1인지 확인
#           오른쪽 칸이 더 크면 그칸에서부터 왼쪽으로 L개가 길이가 같은지 확인.
#           중간에 길이가 달라지거나 L개가 되기 전에 범위를 벗어나거나 이미 경사로가 놓여있으면 못 놓음

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(arr):
    n = len(arr)
    placed = [False] * n
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            diff = abs(arr[i]-arr[i-1])
            if diff != 1:
                return False
            if arr[i-1] < arr[i]: # 오른쪽이 더 높은 경우
                for j in range(1, L+1):
                    if i-j < 0: # 경사로의 범위가 넘어가는 경우. 이걸 제일 위에서 확인해서 밑에꺼가 index out of range 안되게 막음
                        return False
                    if arr[i-1] != arr[i-j]: # 연속되지 않는 경우. 중간에 하나라도 높이가 달라지면
                        return False
                    if placed[i-j]: # 이미 경사로가 놓여있는 경우
                        return False
                    placed[i-j] = True
            else: # 왼쪽이 더 높은 경우
                for j in range(L):
                    if i+j >= n: # 경사로의 범위가 넘어가는 경우
                        return False
                    if arr[i] != arr[i+j]: # 연속되지 않는 경우. 중간에 하나라도 높이가 달라지면
                        return False
                    if placed[i+j]: # 이미 경사로가 놓여있는 경우
                        return False
                    placed[i+j] = True
    return True

ans = 0
# 각 행들 검사
for i in range(N):
    a = board[i]
    if check(a):
        ans += 1
# 각 열들 검사
for j in range(N):
    a = [board[i][j] for i in range(N)]
    if check(a):
        ans += 1
print(ans)


