from collections import deque
N = int(input())
nums = list(map(int, input().split()))
q = deque()
for i in range(N):
    q.append((nums[i], i+1))
ans = []
idx = 0
while q:
    tmp = q.popleft()
    ans.append(tmp[1])
    if tmp[0] > 0:
        cnt = 1
        while cnt < tmp[0] and q:
            t = q.popleft()
            q.append(t)
            cnt += 1
    elif tmp[0] < 0:
        cnt = 0
        while cnt < abs(tmp[0]) and q:
            t = q.pop()
            q.appendleft(t)
            cnt += 1
print(*ans)

'''
-3 -1 2 1
'''