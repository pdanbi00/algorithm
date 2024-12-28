import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ice = [[False] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1
print(result)