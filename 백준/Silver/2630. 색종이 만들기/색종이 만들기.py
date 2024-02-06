N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
w_count = 0
b_count = 0
paper_list = []
l_size = N
l_count = N // l_size

def check(arr):
    global w_count, b_count
    l = len(arr)
    c = arr[0][0]
    b = [[0]*(l//2) for _ in range(l//2)]
    possible = True
    for i in range(l):
        for j in range(l):
            if arr[i][j] != c:
                possible = False
                break
        if not possible:
            break
    else:
        if c == 1:
            b_count += 1
        else:
            w_count += 1
    if not possible:
        for i in range(2):
            for j in range(2):
                for k in range(l//2):
                    for p in range(l//2):
                        b[k][p] = arr[i*(l//2)+k][j*(l//2)+p]
                check(b)

check(board)
print(w_count)
print(b_count)
