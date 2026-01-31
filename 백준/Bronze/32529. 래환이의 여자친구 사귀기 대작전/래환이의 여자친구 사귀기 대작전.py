N, M = map(int, input().split())
diet = list(map(int, input().split()))

tmp = 0
answer = -1
for i in range(N-1, -1, -1):
    tmp += diet[i]
    if tmp >= M:
        answer = i + 1
        break

print(answer)