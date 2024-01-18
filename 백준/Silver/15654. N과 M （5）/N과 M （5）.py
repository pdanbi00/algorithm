N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M
used = [False] * N

def func(index, M):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        if not used[i]:
            ans[index] = nums[i]
            used[i] = True
            func(index+1, M)
            used[i] = False

func(0, M)