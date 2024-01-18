N, M = map(int, input().split())

ans = [0] * M

def func(index, M):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
        ans[index] = i
        func(index+1, M)
func(0, M)