h, m = input().split(":")
nums = {'1' : (0, 0), '2': (0, 1), '3' : (0, 2), '4': (1, 0), '5':(1, 1), '6':(1, 2), '7':(2, 0), '8':(2, 1), '9':(2, 2), '0':(3, 1)}
hours = []
minutes = []

hour = int(h)
hours.append(h)
minute = int(m)
minutes.append(m)
for i in range(4):
    hour += 24
    if hour <= 99:
        hours.append(''.join(str(hour)))
    minute += 60
    if minute <= 99:
        minutes.append(''.join(str(minute)))


answer = 10**9
a_h = ''
a_m = ''
for h in hours:
    for m in minutes:
        tmp = 0
        tmp += abs(nums[h[1]][0] - nums[h[0]][0]) + abs(nums[h[1]][1] - nums[h[0]][1])
        tmp += abs(nums[h[1]][0] - nums[m[0]][0]) + abs(nums[h[1]][1] - nums[m[0]][1])
        tmp += abs(nums[m[1]][0] - nums[m[0]][0]) + abs(nums[m[1]][1] - nums[m[0]][1])
        if tmp < answer:
            answer = tmp
            a_h, a_m = h, m
print(a_h + ':' + a_m)