N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]

medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)
for i in range(N):
    if medals[i][0] == K:
        idx = i
for j in range(N):
    if medals[j][1:] == medals[idx][1:]:
        print(j+1)
        break