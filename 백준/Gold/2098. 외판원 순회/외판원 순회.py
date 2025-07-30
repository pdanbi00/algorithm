import sys
input = sys.stdin.readline

N = int(input())
INF = int(1e9)


graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(x, bitState):
    if (bitState == (1 << N) - 1): # 모든 도시를 방문 했다면
        if (graph[x][0] != 0): # x에서 출발점으로 갈 수 있다면
            return graph[x][0]
        else: # 출발점으로 갈 수 없을 경우
            return INF

    if dp[x][bitState] != -1: # 이미 최소비용이 계산되어 있을 경우
        return dp[x][bitState]

    dp[x][bitState] = INF
    for i in range(N):
        if graph[x][i] == 0 or (bitState & (1 << i) > 0): # 경로가 있고 방문하지 않은 경우
            continue
        dp[x][bitState] = min(dp[x][bitState], tsp(i, bitState | (1 << i)) + graph[x][i])

    return dp[x][bitState]

# 시작 지점은 어느 집이 되어도 상관없음
# 0 → 1 → 2 → 3 → 0랑 2 → 3 → 0 → 1 → 2처럼 순회하는 경로의 정답은 동일함.
print(tsp(0, 1))