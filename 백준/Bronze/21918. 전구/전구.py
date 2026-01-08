import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lights = list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        lights[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            lights[i] = (lights[i] + 1) % 2
    elif a == 3:
        for i in range(b-1, c):
            lights[i] = 0
    elif a == 4:
        for i in range(b-1, c):
            lights[i] = 1

print(*lights)