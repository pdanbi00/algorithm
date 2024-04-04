# 네잎클로버 위치가 -100,000부터 100,000까지니깐
# 200,000 으로 만들어서 100,000이 원점이다 생각하고 ㄱ
N, M = map(int, input().split())
clover_x = [[] for _ in range(200000)]
clover_y = [[] for _ in range(200000)]
for i in range(N):
    x, y = map(int, input().split())
    clover_x[x+100000].append(y+100000)
    clover_y[y+100000].append(x+100000)
for i in range(200000):
    if len(clover_x[i]) > 0:
        clover_x[i].sort()
    if len(clover_y[i]) > 0:
        clover_y[i].sort()

command = input()
x = 100000
y = 100000
for com in command:
    if com == 'L':
        # 왼쪽으로 움직이는 경우
        max = len(clover_y[y])
        for i in range(max-1, -1, -1):
            if clover_y[y][i] < x:
                x = clover_y[y][i]
                break
    elif com == 'R':
        # 오른쪽으로 움직이는 경우
        max = len(clover_y[y])
        for i in range(max):
            if clover_y[y][i] > x:
                x = clover_y[y][i]
                break
    elif com == 'U':
        # 위쪽으로 움직이는 경우
        max = len(clover_x[x])
        for i in range(max):
            if clover_x[x][i] > y:
                y = clover_x[x][i]
                break
    elif com == 'D':
        # 아래쪽으로 움직이는 경우
        max = len(clover_x[x])
        for i in range(max-1, -1, -1):
            if clover_x[x][i] < y:
                y = clover_x[x][i]
                break
print(x-100000, y-100000)