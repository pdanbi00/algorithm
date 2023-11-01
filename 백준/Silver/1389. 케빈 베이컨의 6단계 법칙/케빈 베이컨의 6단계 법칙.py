from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
friends = [[] for _ in range(N+1)]

def bfs(start):
    nums = [0] * (N+1)
    visited = [0] * (N+1)

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for next in friends[x]:
            if not visited[next]:
                nums[next] = nums[x] + 1
                visited[next] = 1
                q.append(next)
    return sum(nums)


for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = 10000000000000
for i in range(1, N+1):
    if bfs(i) < answer:
        answer = bfs(i)
        person = i
print(person)