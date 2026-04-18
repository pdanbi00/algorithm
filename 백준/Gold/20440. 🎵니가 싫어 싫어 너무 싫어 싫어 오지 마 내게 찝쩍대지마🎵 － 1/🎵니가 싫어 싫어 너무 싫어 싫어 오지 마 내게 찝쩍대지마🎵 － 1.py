import sys
input = sys.stdin.readline
N = int(input())

mosquito = []
timeline = dict()

# 입장은 +1, 퇴장은 -1로 기록
for _ in range(N):
    e, x = map(int, input().split())

    if e in timeline:
        timeline[e] += 1
    else:
        timeline[e] = 1

    if x in timeline:
        timeline[x] -= 1
    else:
        timeline[x] = -1


time = list(timeline.keys())
time.sort()

sum = 0
max = 0
ans_s = 0
ans_e = 0

opened = False # 최대 구간이 열렸는지

for k in time:
    sum += timeline[k] # +1 or -1값들을 누적시켜서 k시간에 몇마리 모기가 있는지 확인

    if sum > max:
        max = sum
        ans_s = k
        opened = True
    elif sum < max and opened:
        ans_e = k
        opened = False

print(max)
print(ans_s, ans_e)