# 별 2개를 기준으로 잡아서 그 2개가 트램펄린의 테두리에 위치하도록 살펴보기
N, M, L, K = map(int, input().split())
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append((x, y))
ans = 1e9
for A in stars:
    for B in stars:
        cnt = 0
        sx, sy = min(A[0], B[0]), min(A[1], B[1])
        for C in stars:
            if sx <= C[0] <= sx+L and sy <= C[1] <= sy+L:
                cnt += 1
        ans = min(ans, K-cnt)
print(ans)