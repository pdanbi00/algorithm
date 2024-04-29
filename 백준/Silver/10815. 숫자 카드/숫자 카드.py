N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
nums = list(map(int, input().split()))

for n in nums:
    l = 0
    r = N-1
    find = False
    while l <= r:
        mid = (l+r) // 2

        if card[mid] > n:
            r = mid - 1

        elif card[mid] < n:
            l = mid + 1

        else:
            find = True
            break
    if find:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

