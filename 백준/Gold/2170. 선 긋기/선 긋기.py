import sys
input = sys.stdin.readline
N = int(input())

lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()

ans = 0

start, end = lines[0]

for i in range(1, N):
    a, b = lines[i]
    # 겹치는 경우
    if a <= end:
        end = max(end, b)
    # 아예 안 겹치는 경우
    else:
        ans += end - start
        start, end = a, b

ans += end - start
print(ans)