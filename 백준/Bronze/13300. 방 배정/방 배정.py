ans = 0
N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    student[Y-1][S] += 1
for i in range(6):
    for j in range(2):
        if student[i][j] > 0:
            if student[i][j] % K == 0:
                ans += student[i][j] // K
            else:
                ans += (student[i][j] // K + 1)
print(ans)