import sys
input = sys.stdin.readline

max_num = 10
min_num = 1
while True:
    num = int(input().rstrip())
    if num == 0:
        break
    answer = input().rstrip()
    if answer == 'right on':
        if num >= min_num and num <= max_num:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        max_num = 10
        min_num = 1
    elif answer == "too high":
        max_num = min(max_num, num-1)
        # print(nums)
    elif answer == 'too low':
        min_num = max(min_num, num+1)
        # print(nums)