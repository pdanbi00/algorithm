import sys
input = sys.stdin.readline

N = int(input())
schedule = []
days = [0] * 366

for _ in range(N):
    s, e = map(int, input().split())
    schedule.append((s, e))

schedule.sort(key=lambda x : (x[0], -x[1]))

for day in schedule:
    for i in range(day[0], day[1]+1):
        days[i] += 1

answer = 0

day = 0
pre = -1
max_cnt = 0
while day <= 365:
    if days[day] > 0:
        if pre == -1:
            pre = day
            max_cnt = days[day]
        else:
            max_cnt = max(max_cnt, days[day])
    else:
        if pre != -1:
            answer += (day - pre) * max_cnt
            pre = -1
            max_cnt = 0

    day += 1

if days[365] > 0:
    answer += (day - pre) * max_cnt
print(answer)