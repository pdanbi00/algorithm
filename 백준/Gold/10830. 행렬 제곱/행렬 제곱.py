import sys
input = sys.stdin.readline

# 행렬 곱셈 함수
def matrix_multi(arr1, arr2):
    # 곱셈 결과 저장할 배열
    a = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                a[i][j] += arr1[i][k] * arr2[k][j] % 1000
    return a

# 분할 정복 함수
def power(n, arr):
    if n == 1:
        return arr
    # n이 짝수일 경우 그냥 계산
    if n % 2 == 0:
        half = power(n//2, arr)
        return matrix_multi(half, half)
    # n이 홀수일 경우 A * (A^B-1)요런 식으로 분할
    else:
        return matrix_multi(arr, power(n-1, arr))


N, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = power(B, board)

for i in range(N):
    for j in range(N):
        result[i][j] = result[i][j] % 1000

for i in range(N):
    print(*result[i])