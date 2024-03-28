N, H = map(int, input().split())
jong = [0] * (H+1) # 종유석
suck = [0] * (H+1) # 석순
for i in range(N):
    height = int(input())
    if i % 2 == 0: # 석순
        suck[height] += 1
    else:
        jong[height] += 1

# 인덱스 역순으로 누적합 계산
for i in range(H-1, -1, -1):
    jong[i] += jong[i+1]
    suck[i] += suck[i+1]

# 최소로 잘리는 장애물 개수
min_count = N

# 최소 높이로 잘리는 구간 수
same_height = 0

# 전체 높이 i 기준, 높이에 따라 잘리는 석순과 종유석 개수 파악
for i in range(1, H+1):
    # 현재까지 최소로 잘린 개수보다 현재 높이에서 잘린 개수가 더 적은 경우 갱신
    if (min_count > suck[i]+jong[H-i+1]):
        min_count = suck[i] + jong[H-i+1]
        same_height = 1
    elif min_count == suck[i]+jong[H-i+1]:
        same_height += 1
print(min_count, same_height)