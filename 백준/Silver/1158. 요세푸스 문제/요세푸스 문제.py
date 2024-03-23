from collections import deque
N, K = map(int, input().split())

q = deque()
for i in range(1, N+1):
    q.append(str(i))
ans = []
print("<", end="")
while N > 0:
    for i in range(K-1):
        n = q.popleft()
        q.append(n)
    ans.append(q.popleft())
    N -= 1
print(', '.join(ans), end="")
print('>')