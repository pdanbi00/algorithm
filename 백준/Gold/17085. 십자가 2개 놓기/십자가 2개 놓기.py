# 주의 : 무조건 최대 크기의 정보만 저장하면 안됨
# 1 * 9보다 5 * 5가 더 큼.

'''
5 8
..#..#..
..#..#..
########
..#..#..
..#..#..

정답 : 25
'''

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dotInfo = []
answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# row, col에서 최대 확장 가능 크기 구하기
def search(row, col):
    size = 0
    while 0 <= row - size and row + size < N and 0 <= col - size and col + size < M and board[row-size][col] == board[row+size][col] == board[row][col - size] == board[row][col + size] == '#':
        size += 1
    while size: # 작은 경우끼리 곱하는 경우가 더 클 수도 있으니 사이즈 줄여봐야 됨.
        dotInfo.append((row, col, size-1))
        size -= 1

# 각 십자가가 서로 안 겹치는지 유효성 검사
def test(dot1, dot2):
    testBoard = [[0] * M for _ in range(N)]
    for i in range(dot1[2]+1): # size가 1일 경우 i는 0밖에 안되는데 그럼 한칸씩 확장해서 살펴볼 수가 없음.
        for k in range(4):
            testBoard[dot1[0] + dr[k] * i][dot1[1] + dc[k] * i] = 1

    for i in range(dot2[2]+1): # size가 1일 경우 i는 0밖에 안되는데 그럼 한칸씩 확장해서 살펴볼 수가 없음.
        for k in range(4):
            if testBoard[dot2[0] + dr[k] * i][dot2[1] + dc[k] * i] == 1:
                return False # 첫번째 십자가랑 겹치면 False 반환
    return True


for i in range(N):
    for j in range(M):
        if board[i][j] == '#':
            search(i, j) # '#'인 부분 정보 저장하기

for i in range(len(dotInfo) - 1):
    for j in range(i+1, len(dotInfo)):
        tmp = (1 + (dotInfo[i][2] * 4)) * (1 + (dotInfo[j][2] * 4))
        # 현재 값보다 큰 경우만 유호성 검사
        if tmp > answer and test(dotInfo[i], dotInfo[j]):
            answer = tmp

print(answer)