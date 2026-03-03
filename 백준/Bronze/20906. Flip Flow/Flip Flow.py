t, s, n = map(int, input().split())
flipped = list(map(int, input().split()))

up = 0
down = s

for i in range(n-1):
    up, down = down, up
    tmp = flipped[i+1] - flipped[i]
    if tmp > up:
        up, down = 0, s
    else:
        up -= tmp
        down += tmp

time = flipped[-1] + down
if time <= t:
    time = 0
else:
    time -= t
print(time)