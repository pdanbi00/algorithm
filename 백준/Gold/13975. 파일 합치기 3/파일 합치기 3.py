# heap 정렬 이용해서 제일 작은 값 2개를 계속해서 더하면 된다.
from heapq import heappush, heappop, heapify
T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapify(files) # 리스트를 힙으로 변경
    ans = 0
    while len(files) > 1:
        a = heappop(files)
        b = heappop(files)
        ans += a + b
        heappush(files, a+b)
    print(ans)
