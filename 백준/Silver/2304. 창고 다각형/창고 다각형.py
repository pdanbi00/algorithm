# 제일 높은 값 앞에는 커지는 방향으로 해야하고,
# 제일 높은 값 뒤에는 작아지는 방향으로 해야 됨.
building = []
N = int(input())
max_height = 0

for i in range(N):
    location, height = map(int, input().split())
    building.append((location, height))
building.sort(key=lambda x : x[0])

# 제일 높은 기둥 번호 알아내기
max_idx = 0
max_v = 0
for i in range(N):
    if building[i][1] > max_v:
        max_idx = i
        answer = building[i][1]
        max_v = building[i][1]
pre = building[0][1]
idx = 0
for i in range(max_idx):
    if pre < building[i+1][1]:
        answer += pre * (building[i+1][0] - building[i][0])
        pre = building[i+1][1]
    else:
        answer += pre * (building[i+1][0] - building[i][0])

# 뒤에서부터도 똑같이
pre = building[-1][1]
for i in range(N-1, max_idx, -1):
    if pre < building[i-1][1]:
        answer += pre * (building[i][0]-building[i-1][0])
        pre = building[i-1][1]
    else:
        answer += pre * (building[i][0] - building[i - 1][0])
print(answer)