N, M = map(int, input().split())

ans = [0] * M
used = [False] * (N+1)
def func(index, N, M):
    if index == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1):
        if not used[i]:
            ans[index] = i
            used[i] = True
            func(index+1, N, M)
            used[i] = False
func(0, N, M)
