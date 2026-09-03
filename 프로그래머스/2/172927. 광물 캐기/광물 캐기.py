from heapq import heappush, heappop

def solution(picks, minerals):
    answer = 0
    q = []
    total = 0
    for i in range(3):
        total += 5 * picks[i]
        
    N = len(minerals)
    for i in range(0, N, 5):
        d, ir, s = 0, 0, 0
        for j in range(5):
            if i + j >= N or i + j >= total:
                break
                
            if minerals[i+j] == "diamond":
                d += 1
            elif minerals[i+j] == "iron":
                ir += 1
            elif minerals[i+j] == "stone":
                s += 1
        heappush(q, (-d, -ir, -s))
    
    tool = 0
    while q:
        d, ir, s = heappop(q)
        
        d *= -1
        ir *= -1
        s *= -1
        
        while tool < 3 and picks[tool] <= 0:
            tool += 1
                
        if tool >= 3:
            break
        
        print(picks, tool, d, ir, s)
            
        if tool == 0 and picks[tool] > 0:
            answer += d + ir + s
        elif tool == 1 and picks[tool] > 0:
            answer += d * 5 + ir + s
        elif tool == 2 and picks[tool] > 0:
            answer += d * 25 + ir * 5 + s
            
        picks[tool] -= 1
        
    return answer

'''
(5, 0, 0) , (0, 5, 0), (1, 0, 0)
(3, 2, 0), (1, 1, 1)

'''