N = int(input())
# 개수 줄어드는 방향
for i in range(N, 0, -1):
    # 빈칸 출력
    for j in range(N-i):
        print(' ', end='')
    # 별 출력
    for j in range(2 * i - 1):
        print('*', end='')
    print(' ')

# 개수 늘어나는 방향
for i in range(2, N+1):
    # 빈칸 출력
    for j in range(N-i):
        print(' ', end='')
    # 별 출력
    for j in range(2 * i - 1):
        print('*', end='')
    print(' ')