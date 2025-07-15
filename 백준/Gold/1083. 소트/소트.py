N = int(input())
nums = list(map(int, input().split()))
S = int(input())

sorted_num = []
cnt = 0
while S > 0:
    if nums == sorted_num:
        break
    if S == 1:
        for i in range(cnt, N-1):
            if nums[i] < nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                break
        break
    nums_idx = []
    for i in range(cnt, N):
        if nums[i] not in sorted_num:
            nums_idx.append((nums[i], i))
    nums_idx.sort(key=lambda x: x[0], reverse=True)
    for i in range(len(nums_idx)):
        if nums_idx[i][1] - cnt <= S:
            for j in range(nums_idx[i][1], cnt, -1):
                nums[j], nums[j-1] = nums[j-1], nums[j]
            S -= nums_idx[i][1] - cnt
            sorted_num.append(nums_idx[i][0])
            break
    cnt += 1
print(*nums)