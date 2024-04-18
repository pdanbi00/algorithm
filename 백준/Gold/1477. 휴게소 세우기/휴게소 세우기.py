N, M, L = map(int, input().split())
hu = [0] + list(map(int, input().split())) + [L]
hu.sort()
start = 1
end = L-1
ans = 0
# 이분 탐색
while start <= end:
    mid = (start+end) // 2 # 가장 멀리 떨어져 있는 휴게소 사이 거리
    count = 0 # 추가한 휴게소 개수
    for i in range(1, len(hu)):
        dist = hu[i] - hu[i-1]
        if dist > mid:
            count += (dist-1) // mid # 현재 휴게소가 설치되어 있는 구역은 제외하기 위해 -1

    if count > M:
        start = mid + 1

    else:
        ans = mid
        end = mid - 1
print(ans)

