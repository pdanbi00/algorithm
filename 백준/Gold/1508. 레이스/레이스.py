# 이진탐색
import sys
input = sys.stdin.readline

# 이진탐색으로 거리를 구하고, 그 거리가 되는 곳들에 심판 배치
N, M, K = map(int, input().split())
judges = list(map(int, input().split()))
l = 1
r = judges[-1] - judges[0]

distance = 0

ans = [0] * K
while l <= r:
    mid = (l+r) // 2
    cnt = 1 # 첫번째 자리에는 무조건 심판이 서 있음.
    prev = judges[0]
    for i in range(1, K):
        if judges[i] - prev >= mid:
            cnt += 1 # 심판 수 증가
            prev = judges[i] # 이전값 갱신

    # 심판의 수가 적으면 거리를 줄여줘야 됨.
    if cnt < M:
        r = mid - 1
    # 심판 수가 많으면 distanced에 저장
    else:
        l = mid + 1
        distance = mid

# 심판 위치 구하기
# 사전순으로 큰 경우 해야하니깐 처음에는 무조건 심판이 서있음
ans = '1'
cnt = 1
prev = judges[0]
for i in range(1, K):
    if judges[i] - prev >= distance and cnt < M:
        ans += '1'
        cnt += 1
        prev = judges[i]

    else:
        ans += '0'
print(ans)