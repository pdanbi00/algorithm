import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9

def func(r, c, d1, d2):
    global answer
    visited = [[0] * N for _ in range(N)]
    # 1번 경계선 긋기
    dr, dc = 0, 0
    while dr <= d1 and dc >= -d1:
        visited[r + dr][c + dc] = 5
        dr += 1
        dc -= 1

    # 2번 경계선 긋기
    dr, dc = 0, 0
    while dr <= d2 and dc <= d2:
        visited[r + dr][c + dc] = 5
        dr += 1
        dc += 1

    # 3번 경계선 긋기
    dr, dc = 0, 0
    while dr <= d2 and dc <= d2:
        visited[r + d1 + dr][c - d1 + dc] = 5
        dr += 1
        dc += 1

    # 4번 경계선 긋기
    dr, dc = 0, 0
    while dr <= d1 and dc >= -d1:
        visited[r + d2 + dr][c + d2 + dc] = 5
        dr += 1
        dc -= 1

    tmp = [0] * 5

    # 1번 선거구 인원수 세기
    for i in range(r+d1):
        for j in range(c+1):
            if visited[i][j] == 5:
                break
            visited[i][j] = 1
            tmp[0] += board[i][j]

    # 2번 선거구 인원수 세기
    for j in range(c+1, N):
        for i in range(r + d2+1):
            if visited[i][j] == 5:
                break
            visited[i][j] = 2
            tmp[1] += board[i][j]

    # 3번 선거구 인원수 세기
    for i in range(r + d1, N):
        for j in range(c - d1 + d2):
            if visited[i][j] == 5:
                break
            visited[i][j] = 3
            tmp[2] += board[i][j]

    # 4번 선거구 인원수 세기
    for i in range(r + d2 + 1, N):
        for j in range(N-1, c - d1 + d2 - 1, -1):
            if visited[i][j] == 5:
                break
            visited[i][j] = 4
            tmp[3] += board[i][j]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 or visited[i][j] == 5:
                tmp[4] += board[i][j]

    diff = max(tmp) - min(tmp)
    answer = min(diff, answer)


for i in range(N): # 행
    for j in range(N): # 열
        for d1 in range(1, N):
            for d2 in range(1, N):
                if (j - d1) >= 0 and (j + d2) < N and (i + d1 + d2) < N:
                    func(i, j, d1, d2)

# func(3, 2, 1, 1)
print(answer)

'''
7
1 2 3 4 1 6 1
7 8 9 1 4 2 2
2 3 4 1 1 3 3
6 6 6 6 9 4 4
9 1 9 1 9 5 5
1 1 1 1 9 9 6
1 1 1 1 9 9 6
'''