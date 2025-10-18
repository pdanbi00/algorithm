N, M = map(int, input().split())
balls = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    balls[i-1], balls[j-1] = balls[j-1], balls[i-1]

print(*balls)