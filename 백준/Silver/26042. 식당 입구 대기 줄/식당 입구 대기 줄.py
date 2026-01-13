from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
q = deque()
max_l = 0
answer = 0
for _ in range(N):
    info = list(map(int, input().split()))
    if info[0] == 1:
        q.append(info[1])
        
    else:
        if len(q) > max_l:
            max_l = len(q)
            answer = q[-1]
        elif len(q) == max_l:
            answer = min(answer, q[-1])
        q.popleft()
        
if len(q) > max_l:
    max_l = len(q)
    answer = q[-1]
elif len(q) == max_l:
    answer = min(answer, q[-1])
    
print(max_l, answer)