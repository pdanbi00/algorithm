from collections import deque

def solution(players, m, k):
    answer = 0
    servers = deque()
    n = len(players)
    for i in range(n):
        need = players[i] // m
                
        while servers:
            server = servers.popleft()
            if server > i:
                servers.appendleft(server)
                break
        
        current = len(servers)
        if current < need:
            answer += need - current
            for j in range(need-current):
                servers.append(i+k)

    return answer