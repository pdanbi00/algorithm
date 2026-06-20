from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    t1 = sum(queue1)
    t2 = sum(queue2)
    
    total = t1 + t2
    if total % 2 == 1:
        return -1
    
    target = total // 2
    for t in q1:
        if t > target:
            return -1
        
    while answer <= 6000000:
        if t1 > t2:
            tmp = q1.popleft()
            q2.append(tmp)
            t1 -= tmp
            t2 += tmp
            answer += 1
        elif t1 < t2:
            tmp = q2.popleft()
            q1.append(tmp)
            t1 += tmp
            t2 -= tmp
            answer += 1
        else:
            return answer
    
    return -1