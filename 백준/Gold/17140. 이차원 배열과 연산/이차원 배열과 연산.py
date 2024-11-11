r, c, k = map(int, input().split())
r -= 1
c -= 1
board = [list(map(int, input().split())) for _ in range(3)]

def R(l_r, l_c):
    new_board = [[0] * 100 for _ in range(100)]
    max_c = 0
    for i in range(l_r):
        r_dict = {}
        for j in range(l_c):
            if board[i][j] != 0:
                if board[i][j] in r_dict:
                    r_dict[board[i][j]] += 1
                else:
                    r_dict[board[i][j]] = 1
            # else:
            #     break
        arr = []
        for ke, value in r_dict.items():
            arr.append((ke, value))
        arr.sort(key=lambda x : (x[1], x[0]))
        new_arr = []
        for a in arr:
            new_arr.append(a[0])
            new_arr.append(a[1])

        if len(new_arr) > 100:
            new_arr = new_arr[:100]
        max_c = max(max_c, len(new_arr))
        for j in range(len(new_arr)):
            new_board[i][j] = new_arr[j]
    return (new_board, l_r, max_c)

def C(l_r, l_c):
    new_board = [[0] * 100 for _ in range(100)]
    max_r = 0
    for j in range(l_c):
        c_dict = {}
        for i in range(l_r):
            if board[i][j] != 0:
                if board[i][j] in c_dict:
                    c_dict[board[i][j]] += 1
                else:
                    c_dict[board[i][j]] = 1
            # else:
            #     break
        arr = []
        for ke, value in c_dict.items():
            arr.append((ke, value))
        arr.sort(key=lambda x : (x[1], x[0]))
        new_arr = []
        for a in arr:
            new_arr.append(a[0])
            new_arr.append(a[1])

        if len(new_arr) > 100:
            new_arr = new_arr[:100]
        max_r = max(max_r, len(new_arr))
        for i in range(len(new_arr)):
            new_board[i][j] = new_arr[i]
    return (new_board, max_r, l_c)

time = 0
find = False
l_r = 3
l_c = 3
while True:
    if time > 100:
        print(-1)
        break
    if l_r >= r and l_c >= c:
        if board[r][c] == k:
            find = True
            print(time)
            break
    if not find:
        time += 1
        if l_r >= l_c:
            board, l_r, l_c = R(l_r, l_c)
        else:
            board, l_r, l_c = C(l_r, l_c)

