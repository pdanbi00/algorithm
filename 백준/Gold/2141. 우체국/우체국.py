# 사람 수의 절반이 넘어가는 지점의 마을을 찾아야 됨...
import sys
input = sys.stdin.readline

N = int(input())
people = 0
locations = []
for _ in range(N):
    X, A = map(int, input().split())
    locations.append((X, A))
    people += A

locations.sort()

cnt = 0
for X, A in locations:
    cnt += A
    if cnt >= people / 2:
        print(X)
        break