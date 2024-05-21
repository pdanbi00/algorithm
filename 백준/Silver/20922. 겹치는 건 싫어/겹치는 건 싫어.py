N, K = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0

counter = [0] * (max(nums) + 1)
max_cnt = 0

while right < N:
    if counter[nums[right]] < K:
        counter[nums[right]] += 1
        right += 1
    else:
        counter[nums[left]] -= 1
        left += 1
    max_cnt = max(max_cnt, right-left)
print(max_cnt)