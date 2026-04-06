n, t = map(int, input().split())
nums = list(map(int, input().split()))

answer = sorted(nums[:t]) + nums[t:]
print(*answer)