from collections import deque
N = int(input())

q = deque()
used = [[N, 5 * N] for _ in range(1000001)]
used[1][0], used[1][1] = 1, 1


q.append((1, 1, 1))
while q:
    length, water, day = q.popleft()

    if day > used[N][0]:
        break

    tmp = length * length
    if tmp <= N and (used[tmp][0] > day + 1 or (used[tmp][0] == day + 1 and used[tmp][1] > water + 5)):
        q.append((tmp, water + 5, day + 1))
        used[tmp][0] = day+1
        used[tmp][1] = water+5

    tmp = length * 3
    if tmp <= N and (used[tmp][0] > day + 1 or (used[tmp][0] == day + 1 and used[tmp][1] > water + 3)):
        q.append((tmp, water + 3, day + 1))
        used[tmp][0] = day + 1
        used[tmp][1] = water + 3

    tmp = length + 1
    if tmp <= N and (used[tmp][0] > day + 1 or (used[tmp][0] == day + 1 and used[tmp][1] > water + 1)):
        q.append((tmp, water + 1, day + 1))
        used[tmp][0] = day + 1
        used[tmp][1] = water + 1

print(used[N][0], used[N][1])