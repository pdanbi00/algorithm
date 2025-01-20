from collections import deque

N = int(input())
nums = list(map(int, input().split()))

q = deque()
for n in nums:
    q.append(([n], 1))
while q:
    arr, cnt = q.popleft()
    if cnt == N:
        print(*arr)
        exit()
    tmp = arr[-1]
    if tmp % 3 == 0:
        a = tmp // 3
        if a in nums:
            q.append((arr + [a], cnt + 1))
    a = tmp * 2
    if a in nums:
        q.append((arr + [a], cnt + 1))