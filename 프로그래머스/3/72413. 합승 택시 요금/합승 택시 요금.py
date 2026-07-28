# 플로이드-워샬 드가자
def solution(n, s, a, b, fares):
    answer = 0
    distance = [[1e9] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        distance[i][i] = 0
        
    for fare in fares:
        distance[fare[0]][fare[1]] = fare[2]
        distance[fare[1]][fare[0]] = fare[2]
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    answer = distance[s][a] + distance[s][b]
    
    for k in range(1, n+1):
        answer = min(answer, distance[s][k] + distance[k][a] + distance[k][b])
    
    return answer