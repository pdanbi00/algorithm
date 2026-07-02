from heapq import heappush, heappop
from collections import deque

def solution(book_time):
    answer = 0
    book_time.sort()
    newtime = []
    N = len(book_time)
    for i in range(N):
        tmp = []
        for j in range(2):
            time = 0
            h, m = book_time[i][j].split(":")
            time += int(h) * 60 + int(m)
            tmp.append(time)
        newtime.append(tmp)
    heap = []
        
    for i in range(N):
        answer = max(answer, len(heap))
        if not heap:
            heappush(heap, (newtime[i][1], newtime[i][0]))
        else:
            tmp = heappop(heap)
            if newtime[i][0] >= tmp[0]+10:
                heappush(heap, (newtime[i][1], newtime[i][0]))
            else:
                heappush(heap, tmp)
                heappush(heap, (newtime[i][1], newtime[i][0]))
    answer = max(answer, len(heap))
    return answer