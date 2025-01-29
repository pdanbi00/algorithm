N = 3
board = [list(map(int, input().split())) for _ in range(3)]
new_arr = [[0] * 3 for _ in range(3)]
visited = [False] * 10
ans = 1e9

def cal():
    total = 0
    for i in range(3):
        for j in range(3):
            total += abs(board[i][j] - new_arr[i][j])

    return total

def check():
    tmp = sum(new_arr[0])

    # 행 확인
    for i in range(3):
        tmp1 = sum(new_arr[i])

        if tmp != tmp1:
            return False

    # 열 확인
    for j in range(3):
        tmp1 = 0
        for i in range(3):
            tmp1 += new_arr[i][j]
        if tmp != tmp1:
            return False

    # 대각선 확인
    tmp1 = new_arr[0][0] + new_arr[1][1] + new_arr[2][2]
    if tmp != tmp1:
        return False
    tmp2 = new_arr[0][2] + new_arr[1][1] + new_arr[2][0]
    if tmp != tmp2:
        return False

    return True

def dfs(depth):
    global ans
    if depth == 9:
        if (check()):
            ans = min(ans, cal())
        return

    for i in range(1, 10):
        if not visited[i]:
            visited[i] = True
            new_arr[depth // 3][depth % 3] = i
            dfs(depth + 1)
            visited[i] = False

dfs(0)
print(ans)