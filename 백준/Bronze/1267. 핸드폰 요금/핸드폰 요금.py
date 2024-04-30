import math
N = int(input())
calls = list(map(int, input().split()))
y = 0
m = 0
for call in calls:
    y += math.ceil((call / 30)) * 10
    if call % 30 == 0:
        y += 10
    m += math.ceil((call / 60)) * 15
    if call % 60 == 0:
        m += 15

if m > y:
    print('Y', y)
elif m < y:
    print('M', m)
else:
    print('Y', 'M', m)