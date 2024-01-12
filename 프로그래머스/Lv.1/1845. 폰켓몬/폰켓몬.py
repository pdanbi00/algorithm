def solution(nums):
    dic = {}
    count = 0
    for num in nums:
        if num not in dic:
            dic[num] = 1
            count += 1
        else:
            dic[num] = dic[num] + 1
    if count < len(nums) // 2:
        return count
    else:
        return len(nums) // 2