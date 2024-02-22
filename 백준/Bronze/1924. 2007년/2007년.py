days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
date = 0
x, y = map(int, input().split())
for i in range(x-1):
    date += days[i]
date += y
print(day[date%7])