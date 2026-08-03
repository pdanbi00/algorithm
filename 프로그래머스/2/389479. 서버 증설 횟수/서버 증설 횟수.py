from heapq import heappush, heappop


def solution(players, m, k):
    answer = 0
    servers = []
    n = len(players)
    for i in range(n):
        user = players[i]
        tmp = []
        cnt = len(servers)
        
        if (user >= (cnt + 1) * m):
            need = user // m
            # if (user-1) % m > 0:
            #     need += 1
            answer += need - cnt

            for _ in range(need - cnt):
                heappush(servers, k)
                
        while servers:
            server = heappop(servers)
            if server - 1 <= 0:
                continue
            tmp.append(server - 1)
            
        while tmp:
            heappush(servers, tmp.pop())

#         if (user >= (cnt + 1) * m):
#             need = user // m
#             # if (user-1) % m > 0:
#             #     need += 1
#             answer += need - cnt

#             for _ in range(need - cnt):
#                 heappush(servers, k-1)
    return answer