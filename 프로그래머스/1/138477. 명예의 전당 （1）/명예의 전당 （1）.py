from heapq import heappush, heappop
def solution(k, score):
    answer = []
    q = []
    N = len(score)
    for i in range(N):
        heappush(q, score[i])
        if len(q) > k:
            heappop(q)
        answer.append(q[0])
    return answer