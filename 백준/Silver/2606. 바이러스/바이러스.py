def dfs(c):
    global ans

    ans += 1
    v[c] = 1

    for n in connect[c]: # c와 연결된 노드 모두 처리
        if not v[n]:
            dfs(n)

N = int(input())
e = int(input()) # 엣지 개수
connect = [[] for _ in range(N+1)] # 컴퓨터 연결 상태를 저장할 리스트
visited = [0] * (N+1)
for i in range(e):
    n1, n2 = map(int, input().split())
    connect[n1].append(n2)
    connect[n2].append(n1)

ans = 0
v = [0] * (N+1) # 방문 표시
dfs(1)
print(ans-1)