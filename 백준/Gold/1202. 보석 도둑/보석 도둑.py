# 보석이 총 N개
# 가방은 K개. 가방에는 최대 한개의 보석만 가능
# 각 가방에 담을 수 있는 최대 무게는 Ci

# 우선순위 큐
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
N, K = map(int, input().split())
jewelry = []
for _ in range(N):
    a, b = map(int, input().split())
    heappush(jewelry, [a, b])
bags = [int(input()) for _ in range(K)]
bags.sort()

# 각 가방에 담을 수 있는 최대 가치의 보석을 담되, 용량이 작은 가방부터 담기
# 가방을 담을 수 있는 무게 순으로 오름차순 정렬
# 각 가방에 담을 수 있는 모든 보석을 찾을때는 최소힙 사용
# 각 가방에 담을 수 있는 모든 보석 중 가장 가치가 큰 보석 찾을 때는 최대힙 사용

answer = 0
tmp_jew = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heappush(tmp_jew, -heappop(jewelry)[1]) # bag에 담을 수 있는 보석의 무게를 내림차순으로 뽑기 위해서
    if tmp_jew:
        answer += -heappop(tmp_jew)
    elif len(jewelry) == 0:
        break

print(answer)