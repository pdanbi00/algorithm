import math
from collections import deque

N = int(input())

data = dict()
day = 0
answer = 10 ** 8
water = 0
data[1] = [answer, water]
data[N] = [0, 0]
q = deque()
q.append(N)

while q:
    cur = q.popleft()
    if N == 0:
        data[1] = [-1, -1]
        break
    if N == 1:
        data[1] = [0, 0]
        break
    if N == 2:
        data[1] = [1, 1]
        break

    if cur <= 1:
        continue

    data1 = cur - 1
    if data1 in data:
        if data[data1][0] > data[cur][0] + 1:
            data[data1][0] = data[cur][0] + 1
            data[data1][1] = data[cur][1] + 1
            q.append(data1)
        elif data[data1][0] == data[cur][0] + 1 and data[data1][1] > data[cur][1] + 1:
            data[data1][1] = data[cur][1] + 1
            q.append(data1)
    else:
        data[data1] = [data[cur][0] + 1, data[cur][1] + 1]
        q.append(data1)

    if cur % 3 == 0:
        data2 = cur // 3
        if data2 in data:
            if data[data2][0] > data[cur][0] + 1:
                data[data2][0] = data[cur][0] + 1
                data[data2][1] = data[cur][1] + 3
                q.append(data2)
            elif data[data2][0] == data[cur][0] + 1 and data[data2][1] > data[cur][1] + 3:
                data[data2][1] = data[cur][1] + 3
                q.append(data2)
        else:
            data[data2] = [data[cur][0] + 1, data[cur][1] + 3]
            q.append(data2)

    if math.sqrt(cur) == int(math.sqrt(cur)):
        if cur != 1:
            data3 = int(math.sqrt(cur))
            if data3 in data:
                if data[data3][0] > data[cur][0] + 1:
                    data[data3][0] = data[cur][0] + 1
                    data[data3][1] = data[cur][1] + 5
                    q.append(data3)
                elif data[data3][0] == data[cur][0] + 1 and data[data3][1] > data[cur][1] + 5:
                    data[data3][1] = data[cur][1] + 5
                    q.append(data3)
            else:
                data[data3] = [data[cur][0] + 1, data[cur][1] + 5]
                q.append(data3)

print(data[1][0] + 1, data[1][1] + 1)