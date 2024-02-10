from heapq import heappop, heappush, heapify
T = int(input())
for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    check = [1] * k
    for i in range(k):
        char, n = input().split()
        n = int(n)
        if char == 'I':
            heappush(min_heap, (n, i))
            heappush(max_heap, (-n, i))
        elif char == 'D':
            # 원소를 제거함과 동시에 해당하는 숫자의 인덱스를 통해 check의 1을 0으로 삭제되었음을 표시.
            if n == 1:
                if max_heap:
                    check[heappop(max_heap)[1]] = 0 # 삭제한거 표시
            if n == -1:
                if min_heap:
                    check[heappop(min_heap)[1]] = 0 # 삭제한거 표시
        # 다음 제거 대상이 될 인덱스에 있는 원소가 이미 다른 쪽에서 지워진 원소면 제거
        while min_heap and check[min_heap[0][1]] == 0:
            heappop(min_heap)
        while max_heap and check[max_heap[0][1]] == 0:
            heappop(max_heap)
    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
