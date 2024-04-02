from sys import stdin
from heapq import heappush, heappop
T = int(stdin.readline().strip())
for _ in range(T):
    M = int(stdin.readline().strip())
    nums = []
    leftHeap = []
    rightHeap = []
    ans = []
    if M % 10 == 0:
        for _ in range(M//10):
            n = list(map(int, stdin.readline().strip().split()))
            nums.append(n)
    else:
        for i in range(M//10 + 1):
            n = list(map(int, stdin.readline().strip().split()))
            nums.append(n)
    cnt = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if len(leftHeap) == len(rightHeap):
                heappush(leftHeap, -nums[i][j])
            else:
                heappush(rightHeap, nums[i][j])
            cnt += 1

            if rightHeap and rightHeap[0] < -leftHeap[0]:
                leftValue = heappop(leftHeap)
                rightValue = heappop(rightHeap)
                heappush(leftHeap, -rightValue)
                heappush(rightHeap, -leftValue)
            if cnt % 2 == 1:
                ans.append(-leftHeap[0])
    print(len(ans))
    for i in range(len(ans)):
        if (i+1) % 10 == 1 and i != 0:
            print()
        print(ans[i], end=' ')
    print()