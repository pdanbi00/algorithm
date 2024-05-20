# 2. 투 포인터
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(input()))
    
left, right = 0, k
answer = 0
while left < N:
    s = set()
    for i in range(left, right):
        s.add(sushi[i % N])
    if c not in s:
        s.add(c)
    
    answer = max(answer, len(s))
    left += 1
    right += 1
print(answer)