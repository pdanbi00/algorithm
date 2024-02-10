from heapq import heappush, heappop
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * k
    for i in range(k):
        char, num = input().split()
        num = int(num)
        if char == "I":
            heappush(max_heap, (-num, i))
            heappush(min_heap, (num, i))
            visited[i] = True
        elif char == "D":
            if num == -1: # 삭제연산시, key 값을 기준으로(i 값) 해당 노드가 다른 힙에서 삭제된 노드인지 확인
                # 이미 상대힙에 의해 삭제된 노드인 경우 삭제되지 않은 노드가 나오는 동안 계속 버리다가 삭제대상 노드가 나오면 삭제
                while min_heap and not visited[min_heap[0][1]]: # 해당 노드가 삭제된 상태
                    heappop(min_heap) # 상대힙에서 이미 삭제된 노드이기 때문에
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
            elif num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
    # 모든 연산이 끝난 이후에도 쓰레기 노드가 들어있을 수 있어서 다 비우기
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")