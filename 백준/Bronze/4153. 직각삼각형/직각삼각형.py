while True:
    a, b, c = map(int, input().split())
    nums = [a, b, c]
    if a == 0 and b == 0 and c == 0:
        break
    else:
        big = max(nums)
        nums.remove(big)
        length = 0
        for i in range(2):
            length += nums[i] * nums[i]
        if big * big == length:
            print('right')
        else:
            print('wrong')