N = int(input())
M = int(input())

walls = [True] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x, y):
        walls[i] = False

idx = 1
cnt = 0
while idx < N+1:
    if walls[idx] == True:
        cnt += 1

    idx += 1
print(cnt)