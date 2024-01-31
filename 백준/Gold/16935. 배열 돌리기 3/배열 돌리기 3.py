def operation1(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = board[n-1-i][j]
    return ans
def operation2(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = board[i][m-1-j]
    return ans
def operation3(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = board[n-1-j][i]
    return ans
def operation4(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = board[j][m-1-i]
    return ans
def operation5(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j+m//2] = board[i][j]
            ans[i+n//2][j+m//2] = board[i][j+m//2]
            ans[i+n//2][j] = board[i+n//2][j+m//2]
            ans[i][j] = board[i+n//2][j]
    return ans
def operation6(a):
    n = len(a)
    m = len(a[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j] = board[i][j+m//2]
            ans[i][j+m//2] = board[i+n//2][j+m//2]
            ans[i+n//2][j+m//2] = board[i+n//2][j]
            ans[i+n//2][j] = board[i][j]
    return ans

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
calcs = list(map(int, input().split()))
for cal in calcs:
    if cal == 1:
        board = operation1(board)
    elif cal == 2:
        board = operation2(board)
    elif cal == 3:
        board = operation3(board)
    elif cal == 4:
        board = operation4(board)
    elif cal == 5:
        board = operation5(board)
    elif cal == 6:
        board = operation6(board)
for i in board:
    print(*i)