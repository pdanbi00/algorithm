import sys
input = sys.stdin.readline
N = int(input())
dots = []
dot_set = set()
for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))
    dot_set.add((x, y))

answer = 0

for i in range(N-1):
    x1, y1 = dots[i][0], dots[i][1]
    for j in range(i+1, N):
        x2, y2 = dots[j][0], dots[j][1]
        if (x1 == x2 or y1 == y2):
            continue
        if (x1, y2) in dot_set and (x2, y1) in dot_set:
            # print((x1, y1), (x2, y2))
            answer += 1
print(answer // 2)