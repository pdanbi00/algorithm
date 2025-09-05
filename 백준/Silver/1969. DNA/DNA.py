N, M = map(int, input().split())
DNA = [input() for _ in range(N)]

answer = ''
hamming_distance = 0
# A, C, G, T
for k in range(M):
    cnt = [0] * 4
    for i in range(N):
        if DNA[i][k] == 'A':
            cnt[0] += 1
        elif DNA[i][k] == 'C':
            cnt[1] += 1
        elif DNA[i][k] == 'G':
            cnt[2] += 1
        elif DNA[i][k] == 'T':
            cnt[3] += 1

    max_v = max(cnt)
    hamming_distance += N - max_v

    if cnt[0] == max_v:
        answer += 'A'
        continue
    elif cnt[1] == max_v:
        answer += 'C'
        continue
    elif cnt[2] == max_v:
        answer += 'G'
        continue
    elif cnt[3] == max_v:
        answer += 'T'
        continue
print(answer)
print(hamming_distance)
