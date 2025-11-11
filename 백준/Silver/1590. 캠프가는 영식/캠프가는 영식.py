import sys
input = sys.stdin.readline
N, T = map(int, input().split())
times = set()
for _ in range(N):
    S, I, C = map(int, input().split())
    for i in range(C):
        times.add(S + (i * I))

times = list(times)
times.sort()
# print(times)
if times[-1] < T:
    print(-1)
elif times[0] > T:
    print(times[0] - T)
else:
    for i in range(len(times)):
        if times[i] >= T:
            ans = times[i]
            break
    print(ans-T)