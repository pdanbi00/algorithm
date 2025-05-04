import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    scores = []
    for _ in range(N):
        a, b = map(int, input().split())
        scores.append((a, b))

    scores.sort(key=lambda x : x[0])
    top = 0
    ans = 1

    for i in range(1, N):
        if scores[top][1] > scores[i][1]:
            ans += 1
            top = i
    print(ans)