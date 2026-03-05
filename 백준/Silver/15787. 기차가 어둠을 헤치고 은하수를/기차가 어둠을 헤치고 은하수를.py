import sys
input = sys.stdin.readline
N, M = map(int, input().split())

train = [0] * N

for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        i, x = command[1]-1, command[2]-1
        train[i] = train[i] | 1 << x
    elif command[0] == 2:
        i, x = command[1]-1, command[2]-1
        train[i] = train[i] & (~(1 << x))
    elif command[0] == 3:
        i = command[1] - 1
        train[i] = train[i] << 1
        train[i] = train[i] % (1 << 20)
    else:
        i = command[1]-1
        train[i] = train[i] >> 1
milky_way = set()

for i in range(N):
    milky_way.add(train[i])

print(len(milky_way))