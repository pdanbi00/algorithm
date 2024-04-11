# 풀이 : 점프하는 최소거리를 mid로 하는 이진 탐색을 함.
#        없앤 돌 개수가 m보다 작으면 start를 mid+1로
#        없앤 돌 개수가 m보다 크면 end를 mid-1로
import sys
input = sys.stdin.readline
d, n, m = map(int, input().split())
rocks = []
for i in range(n):
    r = int(input())
    rocks.append(r)
rocks.sort()
start = 0
end = d
ans = 0
# 이분탐색
while start <= end:
    mid = (start+end) // 2
    count = 0 # 제거한 돌 개수
    pre_rock = 0 # 이전 바위 위치
    for rock in rocks:
        dist = rock - pre_rock
        if dist < mid: # 거리가 커트라인 보다 작으면 제거
            count += 1
        else:
            pre_rock = rock

    if count > m: # 제거된 돌이 너무 많으면 거리를 크게 가정한거라서 거리를 줄여야 됨
        end = mid-1
    else:
        ans = mid
        start = mid + 1
print(ans)