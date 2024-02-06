N = int(input())
info = []
for i in range(N):
    s, e = map(int, input().split())
    info.append((s, e))
info.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = info[0][1]
for i in range(1, N):
    if info[i][0] >= end:
        cnt += 1
        end = info[i][1]
print(cnt)
