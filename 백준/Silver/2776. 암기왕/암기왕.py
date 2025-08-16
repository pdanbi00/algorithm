import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    nums1 = list(map(int, input().split()))
    nums = set(nums1)
    M = int(input())
    nums2 = list(map(int, input().split()))
    for i in range(M):
        if nums2[i] in nums:
            print(1)
        else:
            print(0)