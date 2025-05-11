import sys
input = sys.stdin.readline
N, K = map(int, input().split())
warrior = [list(map(int, input().split())) for _ in range(N)]
ans = 1000000 * 3
# 모든 경우 다 살펴봄


for i in range(N): # power를 몇번째 용사의 값으로 기준을 잡을지
    for j in range(N): # speed를 몇번째 용사의 값으로 기준을 잡을지
        for k in range(N): # brain을 몇번째 용사의 값으로 기준을 잡을지
            cnt = 0

            for p in range(N):
                if warrior[i][0] >= warrior[p][0] and warrior[j][1] >= warrior[p][1] and warrior[k][2] >= warrior[p][2]:
                    cnt += 1
                    if cnt == K:
                        ans = min(ans, warrior[i][0] + warrior[j][1] + warrior[k][2])

print(ans)