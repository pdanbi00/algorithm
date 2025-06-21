T = int(input())
for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    possible = True
    answer = [0] * N

    for i in range(N):
        if R[i] > i:
            possible = False
            break
    num = 1
    visited = [False] * N
    while num <= N:
        zero_idx = 0
        for i in range(N):
            if R[i] == 0 and not visited[i]:
                zero_idx = i

        answer[zero_idx] = num
        for i in range(zero_idx + 1, N):
            if R[i] != 0:
                R[i] -= 1
        visited[zero_idx] = True
        num += 1

    if possible:
        print(*answer)
    else:
        print("IMPOSSIBLE")
