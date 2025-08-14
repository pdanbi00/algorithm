from heapq import heappush, heappop
N = int(input())
total = int(input())
recommend = list(map(int, input().split()))
now = []

heap = []
for i in range(total):
    if recommend[i] not in now:
        if len(heap) < N:
            now.append(recommend[i])
            heappush(heap, (1, i, recommend[i]))
        else:
            tmp = heappop(heap)
            now.remove(tmp[2])
            now.append(recommend[i])
            heappush(heap, (1, i, recommend[i]))
    else:
        heap2 = []
        while heap:
            tmp = heappop(heap)
            if tmp[2] == recommend[i]:
                heappush(heap, (tmp[0]+1, tmp[1], tmp[2]))
                break
            heappush(heap2, tmp)
        while heap2:
            tmp = heappop(heap2)
            heappush(heap, tmp)

now.sort()
print(*now)