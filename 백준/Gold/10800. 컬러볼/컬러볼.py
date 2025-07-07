import sys
input = sys.stdin.readline
N = int(input())
balls = []

for i in range(N):
    color, size = map(int, input().split())
    balls.append((size, color, i))

balls.sort(key=lambda x : (x[0], x[1], x[2]))
color_count = [0] * 200001
total = 0
j = 0
ans = [0] * (N)

for i in range(N):
    while balls[j][0] < balls[i][0]: # 내 공 크기보다 사이즈가 작아야 잡을 수 있음.
        color_count[balls[j][1]] += balls[j][0] # 각 색깔에 해당하는 총 공의 크기
        total += balls[j][0]
        j += 1
    # 누적합 계산
    # 나보다 작은 공들의 크기 총합에서 나랑 색 같은 것들은 빼주기
    ans[balls[i][2]] = total - color_count[balls[i][1]]

for i in range(N):
    print(ans[i])