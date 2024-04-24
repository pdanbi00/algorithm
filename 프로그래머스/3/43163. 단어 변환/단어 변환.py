from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)
    while q:
        now, count = q.popleft()
        if now == target:
            return count
        for i in range(len(words)):
            if not visited[i]:
                cnt = 0
                for j in range(len(begin)):
                    if now[j] != words[i][j]:
                        cnt += 1
                if cnt == 1:
                    q.append((words[i], count + 1))
                    
                    visited[i] = True
    return 0