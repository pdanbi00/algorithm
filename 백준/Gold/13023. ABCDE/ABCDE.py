import sys
input = sys.stdin.readline
N, M = map(int, input().split())
relations = [[] for _ in range(N)]
# 방문 표시
visited = [False] * N
# 정답인지 판단
ans = False

for i in range(M):
    v1, v2 = map(int, input().split())
    relations[v1].append(v2)
    relations[v2].append(v1)

# dfs
def dfs(index, depth):
    global ans
    visited[index] = True
    # 친구관계가 4번 이상 연결되어 있으면
    if depth == 4:
        ans = True
        return
    # 친구관계가 존재하는지 확인
    for i in relations[index]:
        # 아직 방문 안했으면
        if not visited[i]:
            visited[i] = True
            # 재귀적으로 수행
            dfs(i, depth+1)
            visited[i] = False

# 0번부터 N-1번까지 확인
for i in range(N):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break
if ans:
    print(1)
else:
    print(0)