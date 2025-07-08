import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    N = arr[0]
    nums = arr[1:]
    nums.sort()
    ans = [1e9] * N
    ans[0] = 0
    for i in range(N):
        tmp = 0
        for j in range(i-1, -1, -1):
            tmp += abs(nums[i] - nums[j])
            ans[i-j] = min(ans[i-j], tmp)
    print(sum(ans))

'''
1 3 4 5 8

2
1, 4
1, 3, 7
3, 4, 5, 7
'''