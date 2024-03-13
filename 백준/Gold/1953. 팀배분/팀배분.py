# 두팀으로 나누기
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    person = list(map(int, input().split()))
    for j in range(1, person[0]+1):
        graph[i].append(person[j])
blue = []
white = []
# dfs로 가서 계속 반대로 넣기
visited = [False] * (n+1)

def dfs(idx, cnt):
    global c
    if cnt % 2 == 0: # 홀수번째들은 blue팀에 넣기
        blue.append(idx)
    else:
        white.append(idx)
    visited[idx] = True
    c += 1
    for next_idx in graph[idx]:
        if not visited[next_idx]:
            dfs(next_idx, cnt + 1)
c = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i, c)
blue.sort()
white.sort()
print(len(blue))
for i in blue:
    print(i, end=' ')
print()
print(len(white))
for i in white:
    print(i, end=' ')
