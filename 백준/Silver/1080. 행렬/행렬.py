N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]

# 뒤집는 함수
def check(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if A[x][y] == '1':
                A[x][y] = '0'
            else:
                A[x][y] = '1';

if (N < 3 or M < 3) and A != B: # 3 x 3보다 작으면서 리스트 A와 리스트B가 다르면 불가능
    answer = -1
else:
    cnt = 0
    # 행렬을 3 x 3으로 뒤집어야하기 때문에 왼쪽 위 모서리 기준으로 확인
    for r in range(N-2):
        for c in range(M-2):
            if A[r][c] != B[r][c]:
                cnt += 1
                check(r, c)
    answer = cnt

    if cnt != -1:
        if A != B:
            answer = -1

print(answer)