N, M = map(int, input().split())

ans = [0] * M

def func(index, start, M):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, N+1):
        ans[index] = i
        func(index+1, i, M)

func(0, 1, M)