N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def func(deepth):
    prev_num = -1

    if deepth == M:
        print(*ans)
        return

    for i in range(N):
        if prev_num != nums[i]:
            ans.append(nums[i])
            prev_num = nums[i]
            func(deepth+1)
            ans.pop()

ans = []
func(0)