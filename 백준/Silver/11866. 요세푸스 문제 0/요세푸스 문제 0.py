# deque 쓰는 방법
from collections import deque
N, K = map(int, input().split())
nums = deque([i for i in range(1, N+1)])

result = []
while nums:
    for i in range(K-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='>')
