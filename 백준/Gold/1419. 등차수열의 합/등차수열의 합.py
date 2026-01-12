from math import ceil, floor
l = int(input())
r = int(input())
k = int(input())

'''
등차수열 합 공식
l <= (k * (2x + (k-1)d)) // 2 <= r

->  (2l // k) <= 2x + (k-1)d <= (2r // k)
'''

# 2 <= k <= 5 범위를 잘 봐야됨
# k = 2 일 경우
# l <= 2x + d <= r
# 즉, 3이상의 모든 자연수는 다 가능함

# k = 3 일 경우
# l / 3 <= x + d <= r / 3
# 2 이상의 모든 자연수는 가능

# k = 4일 경우
# l / 2 <= (2x + 3d) <= r / 2
# 계산 해보면 1, 2, 3, 4, 6 제외하고는 다 됨

# k = 5 일 경우
# l / 5 <= x + 2d <= r / 5
# 3 이상의 모든 수 가능


if k == 2:
    print(max(0, r - max(l, 3) + 1)) # r-max(l,3)+1이 음수가 될 수 있어서 0이랑 max로 비교해주기
elif k == 3:
    l = ceil(l/3)
    r = floor(r/3)
    print(max(0, r - max(l, 2) + 1))
elif k == 4:
    l = ceil(l/2)
    r = floor(r/2)
    tmp = r - l + 1
    if l <= 1 <= r:
        tmp -= 1
    if l <= 2 <= r:
        tmp -= 1
    if l <= 3 <= r:
        tmp -= 1
    if l <= 4 <= r:
        tmp -= 1
    if l <= 6 <= r:
        tmp -= 1
    print(max(0, tmp))
else:
    l = ceil(l/5)
    r = floor(r/5)
    print(max(0, r - max(l, 3) + 1))