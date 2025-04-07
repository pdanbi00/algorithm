import sys
input = sys.stdin.readline
N = int(input())

lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort(key=lambda x : (-x[1], x[0]))

ans = 0

start, end = 1000000000, 1000000000

for i in range(N):
    a, b = lines[i]
    if b < start:
        ans += b - a
        start, end = a, b
    elif start <= b <= end and a < start:
        ans += start - a
        start = a

print(ans)