N = int(input())
M = int(input())
materials = list(map(int, input().split()))

materials.sort()
cnt = 0
used = [False] * N

for i in range(N):
    for j in range(i+1, N):
        if not used[j] and materials[i] + materials[j] == M:
            used[i] = True
            used[j] = True
            cnt += 1

print(cnt)