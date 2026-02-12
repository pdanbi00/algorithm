nums = [i for i in range(1, 11)]
possible = True
while True:
    num = int(input())
    if num == 0:
        break
    answer = input()
    if answer == 'right on':
        if num in nums:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        nums = [i for i in range(1, 11)]
    elif answer == "too high":
        tmp = []
        for n in nums:
            if n < num:
                tmp.append(n)
        nums = tmp
        # print(nums)
    elif answer == 'too low':
        tmp = []
        for n in nums:
            if n > num:
                tmp.append(n)
        nums = tmp
        # print(nums)