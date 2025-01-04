# 각 행마다 하나의 퀸을 둬야 됨
# 오른쪽 위를 향하는 대각선에 포함된 좌표들은 r + c의 값이 모두 동일함
# 오른쪽 아래를 향하는 대각선에 포함된 좌표들은 r-c의 값이 동일함
# 단, r-c가 음수가 나올 수 있기 때문에 N-1 + r-c로 확인

# 재귀함수 호출 횟수를 퀸을 놓으려는 행 번호로 활용, 몇개의 퀸을 놓았는지도 파악 가능

def dfs(idx):
    # 상하좌우 : r, c 좌표 확인
    # 대각선 : y = x 대각선(used_up) r + c가 같으면
    #         y = -x 대각선(used_down) r - c가 같으면
    global ans

    if idx == N:
        ans += 1
        return

    for i in range(N):
        if not used_c[i] and not used_up[idx + i] and not used_down[((N-1) + (idx - i))]:
            used_c[i] = True
            used_up[idx+i] = True
            used_down[(N-1) + (idx - i)] = True
            dfs(idx+1)
            used_c[i] = False
            used_up[idx + i] = False
            used_down[(N - 1) + (idx - i)] = False

N = int(input())

board = [[0] * N for _ in range(N)]
# 열 점유 여부
used_c = [False] * N
# y = x 대각선 점유 여부
used_up = [False] * (2 * (N-1) + 1)
# y = -x 대각선 점유 여부
used_down = [False] * (2 * (N-1) + 1)

ans = 0
dfs(0)
print(ans)