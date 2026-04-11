A, B, C, N = map(int, input().split())

possible = False
for i in range(N):
    if A * i > N:
        break
    for j in range(N):
        if A * i + B * j > N:
            break

        for k in range(N):
            tmp = A * i + B * j + C * k
            if tmp > N:
                break

            if tmp == N:
                possible = True
                break
        if possible:
            break
    if possible:
        break

if possible:
    print(1)
else:
    print(0)