N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

p, q = -1, -1
value = -(10 ** 18)

# dp[L-1][R+1] = dp[L][R] + A[L-1]*B[R+1] + A[R+1]*B[L-1]
# L == R 이라면 dp[L][R] = A[L] * B[R]

for X in range(N):
    for Y in range(X, X+2):
        L, R = X, Y

        if L == R:
            v = -(A[L] * B[R])
        else:
            v = 0

        while L >= 0 and R <= N-1:
            v += (A[L] * B[R] + A[R] * B[L])

            if v > value:
                value = v
                p = L
                q = N-1-R

            R += 1
            L -= 1

print(p, q)
print(value)