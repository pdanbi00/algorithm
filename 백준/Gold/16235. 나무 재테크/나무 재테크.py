from collections import deque
N, M, K = map(int, input().split())
board = [[5] * N for _ in range(N)]
biryo = [list(map(int, input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)] # 현재 심겨져 있는 나무
for _ in range(M):
    r, c, age = map(int, input().split())
    tree[r-1][c-1].append(age)
dead = [[deque() for _ in range(N)] for _ in range(N)] # 위치별로 죽은 나무 저장


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            l = len(tree[i][j])
            # 현재 위치 나무 탐색
            for k in range(l):
                # 나무 성장가능
                if board[i][j] >= tree[i][j][k]:
                    board[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else: # 나무 성장 불가능
                    # 이 이후로 있는 나무들은 양분 부족하기 때문에
                    for _ in range(k, l):
                        # 여름(전부 없애고 양분으로 만들기)
                        board[i][j] += tree[i][j].pop() // 2
                    break

    #가을
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for k in range(8):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if 0 <= nr < N and 0 <= nc < N:
                            tree[nr][nc].appendleft(1)
            # 겨울
            board[i][j] += biryo[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)

'''
5 3 3
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
1 1 2
'''