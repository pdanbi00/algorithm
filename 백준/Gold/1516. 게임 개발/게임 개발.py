from collections import deque
N = int(input())
dp = [0] * (N+1)
arr = [0]
q = deque()
for i in range(1, N+1):
    time, *pre, end = map(int, input().split())
    q.append(i)
    arr.append([i, time, pre, end])

while q:
    i = q.popleft()
    idx, time, pre, end = arr[i]
    possible = True
    for p in pre:
        if dp[p] == 0:
            possible = False
            break
    if possible:
        dp[idx] = time
        for j in pre:
            dp[idx] = max(dp[idx], dp[j] + time)
    else:
        q.append(idx)
for i in range(1, N+1):
    print(dp[i])
