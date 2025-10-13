N = int(input())
info = []
for _ in range(N):
    team_num, time = input().split()
    team_num = int(team_num)
    m, s = time.split(":")
    time = int(m) * 60 + int(s)
    info.append([team_num, time])
    info.sort(key=lambda x : x[1])

a_point = 0
b_point = 0

a_time = 0
b_time = 0

now = 0

for t, time in info:
    if t == 1:
        if a_point > b_point:
            a_time += time - now
        elif a_point < b_point:
            b_time += time - now

        a_point += 1

    else:
        if b_point > a_point:
            b_time += time - now
        elif b_point < a_point:
            a_time += time - now

        b_point += 1

    now = time

if a_point > b_point:
    a_time += 48 * 60 - now

elif b_point > a_point:
    b_time += 48 * 60 - now

m = str(a_time // 60)
t = str(a_time % 60)
if len(m) < 2:
    m = '0' + m

if len(t) < 2:
    t = '0' + t

print(m + ":" + t)

m = str(b_time // 60)
t = str(b_time % 60)
if len(m) < 2:
    m = '0' + m

if len(t) < 2:
    t = '0' + t

print(m + ":" + t)