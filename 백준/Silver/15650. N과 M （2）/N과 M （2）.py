N, M = map(int, input().split())

used = [False] * (N+1)
ans = [0] * M

def func(index, start, M):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, N+1):
        if start <= N:
            if not used[i]:
                ans[index] = i
                used[i] = True
                func(index+1, i+1, M)
                used[i] = False
func(0, 1, M)