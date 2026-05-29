from collections import deque

def solution(x, y, n):
    answer = 1000001
    q = deque()
    q.append((y, 0))
    while q:
        num, cnt = q.popleft()
        if num == x:
            answer = min(answer, cnt)
            break

        if num % 3 == 0:
            q.append((num // 3, cnt+1))
            
        if num % 2 == 0:
            q.append((num // 2, cnt+1))
            
        if num - n >= x:
            q.append((num - n, cnt+1))
            
    if answer == 1000001:
        answer = -1
    
    return answer