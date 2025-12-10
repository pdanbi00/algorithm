N = int(input())
birth = []
for _ in range(N):
    name, day, month, year = input().split()
    if len(day) == 1:
        day = '0' + day

    if len(month) == 1:
        month = '0' + month

    date = year + month + day

    birth.append([date, name])
birth.sort()
print(birth[-1][1])
print(birth[0][1])