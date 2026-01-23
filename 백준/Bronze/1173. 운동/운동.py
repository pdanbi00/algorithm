N, m, M, T, R = map(int, input().split())
time = 0
X = m
recent = m
while N > 0:
    if X + T <= M:
        N -= 1
        X += T
    else:
        if X-R < m:
            X = m
        else:
            X -= R

        if X == recent:
            print(-1)
            exit()
    recent = X
    time += 1

print(time)