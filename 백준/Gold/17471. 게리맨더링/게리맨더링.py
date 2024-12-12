from collections import deque
N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        graph[i].append(info[j])

# 백트래킹으로 도시 나누기
# 분할한 도시가 연결되는지 bfs로 확인 및 합 계산
# 최소값 갱신

def bfs(arr):
    q = deque()
    visited = [False] * (N+1)
    q.append(arr[0])
    visited[arr[0]] = True
    total_people = 0
    count = 1
    while q:
        now = q.popleft()
        total_people += people[now]
        for next_node in graph[now]:
            if next_node in arr and visited[next_node] == False:
                visited[next_node] = True
                count += 1
                q.append(next_node)
    if count == len(arr):
        return total_people
    return -1

def choose(n, cnt): # n : 뽑을 도시 수, cnt : 지금까지 뽑은 도시 수
    global answer
    if n == cnt:
        area1, area2 = [], []
        for i in range(1, N+1):
            if visited[i]:
                area1.append(i)
            else:
                area2.append(i)

        a, b = bfs(area1), bfs(area2) # 두 구역들이 내부적으로 다 연결되어 있는지 확인
        if a != -1 and b != -1:
            answer = min(answer, abs(a-b))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            choose(n, cnt+1)
            visited[i] = False



answer = 1e9
# 도시 분할하기
for i in range(1, N//2 + 1):
    visited = [False] * (N+1)
    choose(i, 0)

if answer == 1e9:
    print(-1)
else:
    print(answer)