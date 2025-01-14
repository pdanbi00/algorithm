A, B, C, X, Y = map(int, input().split())

if A + B < C * 2:
    ans = 0
    ans += A * X
    ans += B * Y
else:
    ans = 0
    ans += 2 * C * min(X, Y)
    ans += min(A, C * 2) * max(0, X - Y)
    ans += min(B, C * 2) * max(0, Y - X)

print(ans)