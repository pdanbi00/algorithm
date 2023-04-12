def solve(idx, M):
    if idx == M:
        for i in range(M):
            print(perm[i], end=' ')
        print()
        return
    for j in range(N):
        if not used[j]:
            perm[idx] = arr[j]
            used[j] = 1
            solve(idx+1, M)
            used[j] = 0

N, M = map(int, input().split())
arr = [x for x in range(1, N+1)]
perm = [0] * M
used = [0] * N
solve(0, M)