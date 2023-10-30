# 아이디어 : DFS를 활용하여 i점과 이어져있는(내 코드에서는 i보다 큰 값)들을 순회하며 방문 체크를 한다.
#           추가로 현재의 나보다 큰값이라면 그 값의 기준에서는 현재의 값은 그 값보다 작은 값이기 때문에 그 값의 입장에서도 방문체크를 한다.
#           DFS로 방문할 수 있는 모든 곳을 방문한 후 행 기준으로 모든 곳이 방문됐다면 정답을 기록한다.

def bfs(now, idx):
    for pre in arr[idx]:
        if not v[now][pre]:
            v[now][pre] = 1
            v[pre][now] = 1
            bfs(now,pre)


N, M = map(int,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    p, c = map(int,input().split())
    arr[p].append(c)

v = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    v[i][i] = 1
    bfs(i,i)



answer = sum([1 if sum(v[i]) == N else 0 for i in range(1,N+1)])
print(answer)