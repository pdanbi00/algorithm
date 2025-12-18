# 점 2개를 골라서 A * B 크기 안에 들어가지는지 확인
import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
dots = []

for i in range(N):
    r, c, s = map(int, input().split())
    dots.append((r, c, s))

answer = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        r = abs(dots[i][0] - dots[j][0])
        c = abs(dots[i][1] - dots[j][1])
        if r < A and c < B:
            answer = max(answer, abs(dots[i][2] - dots[j][2]))

print(answer)