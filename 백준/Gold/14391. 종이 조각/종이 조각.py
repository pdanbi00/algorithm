N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = -1
# 0: 가로     1: 세로
for i in range(1<<(N*M)):
    visited = [False] * (N*M)
    nums = 0
    for j in range(N*M-1, -1, -1):
        ga = 0
        sero = 0
        if i & (1 << j) == 0 and not visited[(N*M - 1)-j]: # 방문하지 않은 가로라면
            visited[(N*M - 1)-j] = True
            ga = board[((N*M - 1)-j)//M][((N*M - 1)-j)%M]
            for k in range(1, M):
                if j - k >= 0:
                    if i & (1 << (j-k)) == 0 and (j-k) % M != (M-1) and not visited[(N*M - 1)-(j-k)]:
                        visited[(N*M - 1)-(j-k)] = True
                        ga += board[((N*M - 1)-(j-k))//M][((N*M - 1)-(j-k))%M]
                    else:
                        break

            nums += int(ga)
        elif i & (1 << j) >0  and not visited[(N*M - 1)-j]: # 방문하지 않은 세로라면
            visited[(N*M - 1)-j] = True
            sero = board[((N*M - 1)-j)//M][((N*M - 1)-j)%M]
            for k in range(1, N):
                if j - (k*M) >= 0:
                    if i & (1 << (j-(k*M))) > 0 and (j-(k*M)) >= 0 and not visited[(N*M - 1)-(j-(k*M))]:
                        visited[(N*M - 1)-(j-(k*M))] = True
                        sero += board[((N*M - 1)-(j-(k*M)))//M][((N*M - 1)-(j-(k*M)))%M]
                    else:
                        break
            nums += int(sero)

    if nums > ans:
        ans = nums
print(ans)