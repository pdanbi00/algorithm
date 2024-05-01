import sys
input = sys.stdin.readline
N = int(input())
now_taps = list(map(int, input().split()))
right_taps = list(map(int, input().split()))

dif_taps = [0] * N
for i in range(N):
    dif_taps[i] = now_taps[i] - right_taps[i]
ans = 0

for i in range(N):
    if dif_taps[i] == 0:
        continue
    if dif_taps[i] > 0:
        x = 1
    else:
        x = -1
    while dif_taps[i] != 0:
        ans += 1
        for j in range(i, N):
            if dif_taps[j] * x <= 0:
                break
            dif_taps[j] -= x
print(ans)