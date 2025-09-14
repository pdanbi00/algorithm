N, L = map(int, input().split())
holes = []
for _ in range(N):
    s, e = map(int, input().split())
    holes.append([s, e])
holes.sort()
answer = 0
idx_h = 0 # 몇 번째 구멍 막아야하는 차례인지
idx_w = holes[0][0] - 1 # 현재까지 널판지 덮은 마지막 위치
while idx_h < N:
    cnt = 0
    if holes[idx_h][0] > idx_w: # 이제 덮을 차례인 구덩이 시작 위치가 현재까지 널판지 덮은 마지막 위치보다 큰 경우
        distance = holes[idx_h][1] - holes[idx_h][0]
        if distance % L > 0:
            cnt = distance // L + 1
        else:
            cnt = distance // L

        # print(distance, cnt)
        idx_w = holes[idx_h][0] + L * cnt - 1
        idx_h += 1
    else: # 이제 덮을 차례인 구덩이 시작 위치가 현재까지 널판지 덮은 마지막 위치보다 작은 경우
        # 이미 idx_h번째 웅덩이가 다 덮인 경우
        if idx_w >= holes[idx_h][1]:
            idx_h += 1
        else:
            distance = holes[idx_h][1] - 1 - idx_w
            if distance % L > 0:
                cnt = distance // L + 1
            else:
                cnt = distance // L
            # print(distance, cnt)
            idx_w += L * cnt
            idx_h += 1
    answer += cnt

print(answer)