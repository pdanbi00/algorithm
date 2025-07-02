N = int(input())
relation = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(1, N):
    graph[relation[i]].append(i)

dp = [0] * N

def dfs(node):
    node_to_sub = []
    for sub in graph[node]:
        dfs(sub)
        node_to_sub.append(dp[sub])

    # 만약 부하직원이 존재한다면
    if node_to_sub:
        # 걸리는 시간을 내림차순으로 정렬. 오래 걸리는 곳을 먼저 주기 위해서
        node_to_sub.sort(reverse=True)
        choose_large_time = []
        for i in range(len(node_to_sub)):
            # node_to_sub[i] : 직속 부하직원에서부터 말단 직원까지 뉴스가 도달하는 데에 걸린 시간
            # i : 뉴스를 전달받는 부하 직원 순서. 뉴스 전달 받기까지 걸리는 대기시간
            choose_large_time.append(node_to_sub[i] + i + 1)
        dp[node] = max(choose_large_time)
dfs(0)
print(dp[0])