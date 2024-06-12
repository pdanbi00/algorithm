# 그리디
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
arr = []
heap = []
for _ in range(N):
    dead, cup = map(int, input().split())
    arr.append((dead, cup))

arr.sort()
# heap 안의 원소의 개수를 데드라인이라고 생각
# heap 안의 원소를 데드라인이 빠른것부터 처리하고, 컵라면 더 많이 가져갈 수 있는데 데드라인에 걸리면 그 전에 넣은 컵라면들 빼면 됨.
for a in arr:
    heappush(heap, a[1])
    if len(heap) > a[0]:
        heappop(heap)
print(sum(heap))

''' 데드라인이 남았는데 삭제하는 경우(여기서 3, 9를 선택하고 3, 4를 지워버리면 안됨.)
3
3 9
3 4
1 1
'''

''' 데드라인이 긴 경우가 더 많은 라면을 얻을 수 있는 경우.(2일꺼 2개 고르면 됨...)
3
1 25
2 50
2 100
'''