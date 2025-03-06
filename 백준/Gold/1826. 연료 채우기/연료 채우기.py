from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

gas_station = []
for _ in range(N):
    a, b = map(int, input().split())
    heappush(gas_station, [a, b])

end, oil = map(int, input().split())

heap = []
answer = 0

# 현재 있는 연료로 마을 갈 수 있을 때까지 반복
while oil < end:
    # 앞으로 주유소가 남아있고, 다음 주유소까지 현재의 연료로 갈 수 있으면
    # 현재 연료로 갈 수 있는 모든 주유소 확인
    while gas_station and gas_station[0][0] <= oil:
        a, b = heappop(gas_station)
        heappush(heap, (-b, a))

    # 현재 연로로 갈 수 있는 주유소가 없다면
    if not heap:
        answer = -1
        break

    # 현재 연료로 갈 수 있는 주유소 중에 주유량이 가장 많은 곳으로
    oil_v, dis = heappop(heap)
    # 연료 충전
    oil += -oil_v
    answer += 1

print(answer)