from heapq import heappush, heappop, heapify
N, M = map(int, input().split())
presents = list(map(int, input().split()))
children = list(map(int, input().split()))
q = []

for i in range(N):
    heappush(q, -presents[i])

impossible = False # 선물이 남아있는지 확인. False이면 선물 다 나눠준거

for child in children:
    x = heappop(q) * -1
    if x - child < 0:
        impossible = True
        break
    heappush(q, -(x - child))

if impossible:
    print(0)
else:
    print(1)