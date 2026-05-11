from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    q = []
    for w in works:
        heappush(q, (-w))
    
    for _ in range(n):
        if q:
            tmp = heappop(q)
            tmp += 1
            if tmp < 0:
                heappush(q, tmp)
        else:
            break
            
    while q:
        tmp = heappop(q)
        answer += tmp * tmp
    return answer