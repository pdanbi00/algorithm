import sys
input = sys.stdin.readline
N = int(input())
x_points = []
y_points = []
for _ in range(N):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)
x_points.append(x_points[0])
y_points.append(y_points[0])

left = 0
right = 0
for i in range(N):
    left += x_points[i] * y_points[i+1]
    right += y_points[i] * x_points[i + 1]

answer = abs(left - right) / 2
print(round(answer, 1))