garo, sero = map(int, input().split())

N = int(input())
garo_list = [0]
sero_list = [0]
for _ in range(N):
    direction, num = map(int, input().split())
    if direction == 1:
        garo_list.append(num)
    else:
        sero_list.append(num)

garo_list.append(garo)
sero_list.append(sero)

garo_list.sort()
sero_list.sort()

max_garo = 0
max_sero = 0

for i in range(len(garo_list)-1):
    tmp = garo_list[i+1] - garo_list[i]
    if tmp > max_garo:
        max_garo = tmp

for i in range(len(sero_list)-1):
    tmp = sero_list[i+1] - sero_list[i]
    if tmp > max_sero:
        max_sero = tmp

print(max_garo * max_sero)