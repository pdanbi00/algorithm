# 구간합
N = int(input())
honey = list(map(int, input().split()))
total = [0]*N
t = 0
for i in range(N):
    t += honey[i]
    total[i] = t
ans = 0

for i in range(1, N-1):
    # 첫번째 경우 : 벌 벌 벌통
    # -> 첫번째 벌은 제일 처음에 고정, 벌통은 제일 뒤에 고정, 중간 벌 위치 조정해서 확인
    # -> 벌은 벌통 방향으로만 이동하기 때문에 벌이 벌통이랑 최대한 멀리 떨어져 있는 곳에서 시작해서 최대한 꿀 많이 따는게 이득임
    s1 = (total[N-1] - total[i]) * 2 + (total[i-1] - total[0])
    # 두번째 경우 : 벌통 벌 벌
    # -> 벌통은 제일 처음에 고정, 두번째 벌 제일 뒤에 고정, 중간 벌 위치 옮기면서 확인
    s2 = total[i-1] * 2 + (total[N-2] - total[i])
    # 세번째 경우 : 벌 벌통 벌
    # -> 벌 양쪽 끝에 고정시키고 벌통 위치 옮겨서 확인
    s3 = total[N-2] - total[i-1] + total[i] - total[0]
    ans = max(ans, s1, s2, s3)

print(ans)



