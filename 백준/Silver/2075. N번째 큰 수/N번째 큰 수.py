# 메모리 초과를 막기 위해서는 힙의 크기를 n으로 유지해야 됨.
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 첫 줄을 min_heap 구조로 넣고
# 그 다음 값들부터는 힙의 최소값보다 큰 값들만 넣어줌.
N = int(input())
nums = []
for _ in range(N):
    arr = list(map(int, input().split()))
    for a in arr:
        if len(nums) < N:
            heappush(nums, a)
        else:
            if nums[0] < a:
                heappop(nums)
                heappush(nums, a)
print(nums[0])