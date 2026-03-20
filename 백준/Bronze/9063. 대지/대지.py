N = int(input())
x1 = 100000
x2 = -100000
y1 = 100000
y2 = -100000

for _ in range(N):
    x, y = map(int, input().split())
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)

print((x2-x1) * (y2-y1))