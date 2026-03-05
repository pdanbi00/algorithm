import sys
input = sys.stdin.readline
N, M = map(int, input().split())

train = [[0] * 20 for _ in range(N)]

for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        i, x = command[1], command[2]
        train[i-1][x-1] = 1
    elif command[0] == 2:
        i, x = command[1], command[2]
        train[i - 1][x - 1] = 0
    elif command[0] == 3:
        i = command[1]
        train[i-1][19] = 0
        for j in range(18, -1, -1):
            train[i-1][j+1] = train[i-1][j]
        train[i-1][0] = 0
    else:
        i = command[1]
        train[i - 1][0] = 0
        for j in range(19):
            train[i - 1][j] = train[i - 1][j+1]
        train[i - 1][19] = 0

milky_way = set()

for i in range(N):
    milky_way.add(tuple(train[i]))

print(len(milky_way))