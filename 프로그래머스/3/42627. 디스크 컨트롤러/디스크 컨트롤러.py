# 현재 시점에서 처리할 수 있는 작업들을 힙에 넣기
from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    now = 0 # 현재시간
    i = 0 # 처리 개수
    start = -1 # 직전 완료 작업의 시작시간
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업 판단
        # 작업 요청 시간이 마지막 완료 작업의 시작시간보다 크고
        # 현재시점보다 작거나 같아야 됨.
        for job in jobs:
            if start < job[0] <= now:
                heappush(heap, (job[1], job[0]))
        
        if heap:
            current = heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return answer // len(jobs)