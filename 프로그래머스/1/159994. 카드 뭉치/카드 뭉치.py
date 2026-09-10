from collections import deque
def solution(cards1, cards2, goal):
    answer = "No"
    q = deque()
    q.append((1, 0, [cards1[0]]))
    q.append((0, 1, [cards2[0]]))
    
    N = len(cards1)
    M = len(cards2)
    
    while q:
        i, j, words = q.popleft()
        if len(words) == len(goal):
            possible = True
            for k in range(len(goal)):
                if goal[k] != words[k]:
                    possible = False
                    break
            if possible:
                answer = "Yes"
                break
            
        elif i + j < len(goal):
            if i < N:
                q.append((i+1, j, words + [cards1[i]]))
            
            if j < M:
                q.append((i, j+1, words + [cards2[j]]))
        
    return answer