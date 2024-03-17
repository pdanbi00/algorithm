def check(list):
    cnt = 0
    for i in range(4):
        if list[i] == 1:
            cnt += 1
    return cnt

for i in range(3):
    nums = list(map(int, input().split()))
    a = check(nums)
    if a == 0:
        print('D')
    elif a == 1:
        print('C')
    elif a == 2:
        print('B')
    elif a == 3:
        print('A')
    else:
        print('E')