# 벨만 포드 : 왜냐면 가중치가 양수가 아닐 수 있고, 모든 정점 다 방문해야해서
import sys
input = sys.stdin.readline

def bellans_ford(start):
    dist[start] = 0
    
	# n번의 라운드를 반복
    for i in range(1, N+1):
        # 매 라운드마다 모든 간선 확인
        for j in range(M):
            now, next, cost = graph[j][0], graph[j][1], graph[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[now] != 1e9 and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                # n번째 라운드에서도 값이 갱신되면 음수 순환 존재
                if i == N:
                    return True
    return False


N, M = map(int, input().split())
graph = []
dist = [1e9] * (N+1)

for _ in range(M):
    start, end, time = map(int, input().split())
    graph.append((start, end, time))
    
negative_cycle = bellans_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])