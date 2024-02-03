def operation1(arr):
    le = len(arr)
    ans = [[0] * le for _ in range(le)]
    for i in range(le):
        for j in range(le):
            ans[i][j] = arr[le-1-i][j]
    return ans

def operation5(arr, l):
    le = len(arr)
    ans = [[0]*le for _ in range(le)]
    sub_size = (1 << l) # 부분 수열 크기
    sub_count = le // sub_size # 부분 수열 개수
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i*sub_size
            y1 = j*sub_size
            x2 = (sub_count-1-i) * sub_size
            y2 = j*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = arr[x2+x][y2+y]
    return ans

def operation2(arr):
    le = len(arr)
    ans = [[0] * le for _ in range(le)]
    for i in range(le):
        for j in range(le):
            ans[i][j] = arr[i][le-1-j]
    return ans

def operation6(arr, l):
    le = len(arr)
    ans = [[0]*le for _ in range(le)]
    sub_size = (1 << l)
    sub_count = le // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i*sub_size
            y1 = j*sub_size
            x2 = i*sub_size
            y2 = (sub_count-1-j)*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = arr[x2+x][y2+y]
    return ans

def operation3(arr):
    le = len(arr)
    ans = [[0]*le for _ in range(le)]
    for i in range(le):
        for j in range(le):
            ans[i][j] = arr[le-1-j][i]
    return ans

def operation7(arr, l):
    le = len(arr)
    ans = [[0]*le for _ in range(le)]
    sub_size = (1 << l)
    sub_count = le // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count-1-j) * sub_size
            y2 = i * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = arr[x2+x][y2+y]
    return ans

def operation4(arr):
    le = len(arr)
    ans = [[0]*le for _ in range(le)]
    for i in range(le):
        for j in range(le):
            ans[i][j]= arr[j][le-1-i]
    return ans

def operation8(arr, l):
    le = len(arr)
    ans = [[0]*le for _ in range(le)]
    sub_size = (1 << l)
    sub_count = le // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = j * sub_size
            y2 = (sub_count-1-i)*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = arr[x2+x][y2+y]
    return ans

# 1부터 4번까지 연산은 부분 수열 내부에서 이뤄짐
# sx, sy는 각 부분 수열에서 제일 왼쪽 위 첫번째칸을 의미
# length는 부분수열 크기
# k는 몇번 연산 수행해야하는지
def operation_1_to_4(board, k, sx, sy, length):
    b = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            b[i][j] = board[sx+i][sy+j]

    if k == 1:
        b = operation1(b)
    elif k == 2:
        b = operation2(b)
    elif k == 3:
        b = operation3(b)
    elif k == 4:
        b = operation4(b)

    for i in range(length):
        for j in range(length):
            board[sx+i][sy+j] = b[i][j]



N, R = map(int, input().split())
size = (1 << N)
board = [list(map(int, input().split())) for _ in range(size)]
for _ in range(R):
    k, l = map(int, input().split())
    sub_size = (1<<l) # l에 따라서 부분 배열의 크기가 s**l이 되니깐
    if 1 <= k <= 4:
        for i in range(0, size, sub_size):
            for j in range(0, size, sub_size):
                operation_1_to_4(board, k, i, j, sub_size)
    elif 5 <= k <= 8:
        if k == 5:
            board = operation5(board, l)
        elif k == 6:
            board = operation6(board, l)
        elif k == 7:
            board = operation7(board, l)
        elif k == 8:
            board = operation8(board, l)

for row in board:
    print(*row)


