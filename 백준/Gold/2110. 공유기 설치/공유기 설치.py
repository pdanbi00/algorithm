# 이분탐색
# 공유기들 사이 거리의 최소값이랑 최대값을 이분탐색해서
# 길이마다 돌면서 설치할 수 있는 공유기 개수 확인해서 변경

N, C = map(int, input().split())
home = []
for i in range(N):
    d = int(input())
    home.append(d)
home.sort()

start = 1
end = home[-1] - home[0]

result = 0
if N == 2:
    # 집이 2개면 무조것 첫번째 집이랑 마지막 집
    print(home[-1] - home[0])
else:
    while start <= end:
        mid = (start + end) // 2 # 공유기를 설치할 간격을 의미함
        current = home[0]
        cnt = 1
        # mid를 공유기 간격으로 했을 때 몇대 설치할 수 있는지 확인
        for i in range(1, N):
            if home[i] >= current + mid:
                cnt += 1
                current = home[i]
        # 공유기 설치 가능한 수가 목표보다 크면 거리 늘림
        if cnt >= C:
            start = mid + 1
            result = mid
        # 공유기 설치 수가 목표보다 작으면 공유기 사이 거리 줄임
        else:
            end = mid - 1
    print(result)

