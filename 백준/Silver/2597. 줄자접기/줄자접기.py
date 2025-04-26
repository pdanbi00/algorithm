right = int(input())
left = 0

points = [list(map(float, input().split())) for _ in range(3)]

for i in range(3):
    a, b = points[i]
    if a == b:
        continue

    mid = (a + b) / 2
    right, left = mid, min(left, (mid * 2 - right))

    for j in range(i+1, 3):
        for k in range(2):
            if points[j][k] > mid:
                points[j][k] = mid * 2 - points[j][k]

print('{:.01f}'.format(right-left))