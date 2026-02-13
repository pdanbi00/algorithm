N, K = map(int, input().split())
blocks = list(map(int, input().split()))

answer = N

for i in range(N):
    base = blocks[i]

    if base > i * K:
        temp_cnt = 0
        for j in range(N):
            if blocks[j] != base + ((j-i) * K):
                temp_cnt += 1
        answer = min(answer, temp_cnt)

print(answer)