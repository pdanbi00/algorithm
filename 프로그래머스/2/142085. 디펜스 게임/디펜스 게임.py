from heapq import heappush, heappop
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    q = []
    for i in range(len(enemy)):
        heappush(q, enemy[i])
        if len(q) > k:
            tmp = heappop(q)
            if n - tmp < 0:
                return i
            n -= tmp
    return len(enemy)