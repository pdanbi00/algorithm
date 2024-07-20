# 재귀임...
# N = 6 -> N=3 3개로 분할 가능
# N = 12 -> N=6 3개로 분할 가능
# N = 24 -> N=12 3개로 분할 가능

N = int(input())

# 1. 전체 배열 생성
board = [[' ']*2*N for _ in range(N)]

# 2. 분할 정복을 위해서 함수 만들기
def recursion(r, c, size):
    # n이 3일때 삼각형 그려주기
    if size == 3:
        board[r][c] = '*'
        board[r+1][c-1] = board[r+1][c+1] = '*'
        for k in range(-2, 3):
            board[r+2][c+k] = '*'
    # n이 3이 아닐 경우 삼각형 분할하기
    else:
        newSize = size // 2
        recursion(r, c, newSize)
        recursion(r+newSize, c-newSize, newSize)
        recursion(r+newSize, c+newSize, newSize)

recursion(0, N-1, N)
for b in board:
    print("".join(b))