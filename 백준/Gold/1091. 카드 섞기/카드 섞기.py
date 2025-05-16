N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

target = [0, 1, 2] * (N // 3)
visited = set()
cnt = 0
answer = -1
while True:
    if target == P:
        answer = cnt
        break
    visited.add(tuple(P))
    tmp = [0] * N
    for i in range(N):
        tmp[S[i]] = P[i]
    cnt += 1
    if tuple(tmp) in visited:
        break
    P = tmp
print(answer)