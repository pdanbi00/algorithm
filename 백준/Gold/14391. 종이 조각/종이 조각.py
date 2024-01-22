N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = -1
# 0: 가로     1: 세로
for i in range(1<<(N*M)):
    visited = [False] * (N*M)
    nums = 0
    for j in range(N*M):
        if i & (1 << j) == 0 and not visited[j]: # 방문하지 않은 가로라면
            visited[j] = True
            ga = board[j//M][j%M]
            for k in range(1, M):
                if i & (1 << (j+k)) == 0 and (j+k) % M != 0 and not visited[j+k]:
                    visited[j+k] = True
                    ga += board[(j+k)//M][(j+k)%M]
                else:
                    break

            nums += int(ga)
        elif i & (1 << j) != 0 and not visited[j]: # 방문하지 않은 tpfh라면
            visited[j] = True
            se = board[j//M][j%M]
            for k in range(1, N):
                if i & (1 << (j+(k*M))) != 0 and (j+(k*M)) < (N*M) and not visited[j+(k*M)]:
                    visited[j+(k*M)] = True
                    se += board[(j+(k*M))//M][(j+(k*M))%M]
                else:
                    break
            nums += int(se)
    if nums > ans:
        ans = nums
print(ans)