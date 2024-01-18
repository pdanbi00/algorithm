N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M

def func(index, M):
    if index == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(N):
        ans[index] = nums[i]
        func(index+1, M)

func(0, M)