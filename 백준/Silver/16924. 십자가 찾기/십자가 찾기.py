import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = []
board = [list(input()) for _ in range(N)]

# 사용한 별인지 체크하기 위한
visited = [[0] * M for _ in range(N)]

# visited가 1이면 아직 사용안한 별
for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            visited[i][j] = 1

def checkStar(i, j, size, visited):
    ans = []
    for s in range(1, size+1):
        if board[i-s][j] == '*' and board[i+s][j] == '*' and board[i][j-s] == '*' and board[i][j+s] == '*':
            ans = [i+1, j+1, s]
            visited[i][j] = 0
            visited[i - s][j] = 0
            visited[i + s][j] = 0
            visited[i][j - s] = 0
            visited[i][j + s] = 0

        else:
            return ans
    return ans

for i in range(1, N-1):
    for j in range(1, M-1):
        if board[i][j] == '*':
            size = min(i, j, N - 1 - i, M - 1 - j)
            ans = checkStar(i, j, size, visited)

            if ans:
                answer.append(ans)

possible = True

for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            possible = False
            break
    if not possible:
        break

if possible:
    print(len(answer))
    for i in range(len(answer)):
        print(*answer[i])

else:
    print(-1)