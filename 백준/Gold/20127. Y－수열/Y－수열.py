N = int(input())
nums = list(map(int, input().split()))

big_sorted_nums = sorted(nums)
small_sorted_nums = sorted(nums, reverse=True)

if small_sorted_nums == nums or big_sorted_nums == nums:
    print(0)
else:
    small_stack = [nums[0]] # 감소 수열
    big_stack = [nums[0]] # 증가 수열
    small_finish = False
    big_finish = False
    small_idx = 1e9
    big_idx = 1e9
    small_nums = []
    big_nums = []
    
    for i in range(1, N):
        if not small_finish:
            if small_stack[-1] >= nums[i]:
                small_stack.append(nums[i])
            else:
                small_nums = nums[i:] + small_stack
                small_finish = True
                small_idx = i
    
        if not big_finish:
            if big_stack[-1] <= nums[i]:
                big_stack.append(nums[i])
            else:
                big_nums = nums[i:] + big_stack
                big_finish = True
                big_idx = i
    
    # print(small_nums)
    # print(big_nums)
    if small_nums == small_sorted_nums and big_nums == big_sorted_nums:
        print(min(small_idx, big_idx))
    elif small_nums == small_sorted_nums:
        print(small_idx)
    elif big_nums == big_sorted_nums:
        print(big_idx)
    else:
        print(-1)