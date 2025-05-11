import sys
input = sys.stdin.readline
N, K = map(int, input().split())
warrior = [list(map(int, input().split())) for _ in range(N)]
ans = 1000000 * 3

powers = []
speeds = []
for i in range(N):
    powers.append(warrior[i][0])
    speeds.append(warrior[i][1])

warrior.sort(key=lambda x : x[2])

for p in powers:
    for s in speeds:
        b = 0
        cnt = 0
        for i in range(N):
            if warrior[i][0] <= p and warrior[i][1] <= s:
                cnt += 1
                z = warrior[i][2]
                if cnt == K:
                    break
        if cnt == K:
            ans = min(ans, p + s + z)

print(ans)