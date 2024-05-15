N, K = map(int, input().split())

nums = [i for i in range(2, N+1)]
cnt = 0
while len(nums) > 0:
    p = nums[0]
    n = p
    for i in range(n, N+1, p):
        if i in nums:
            cnt += 1
            if cnt == K:
                print(i)
                break
            nums.remove(i)
