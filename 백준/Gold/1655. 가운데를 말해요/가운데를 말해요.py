# 우선순위 큐
'''
풀이 방식 : 중간값을 구해야하기 때문에 중간값보다 작은 값은 leftHeap, 큰값은 rightHeap에 넣음
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
leftHeap = [] # 중간값보다 작은 수가 들어감. 최대힙
rightHeap = [] # 중간값보다 큰 수가 들어감. 최소힙
for i in range(N):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, -num)
    else:
        heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heappop(leftHeap)
        rightValue = heappop(rightHeap)

        heappush(leftHeap, -rightValue)
        heappush(rightHeap, -leftValue)
    print(-leftHeap[0])