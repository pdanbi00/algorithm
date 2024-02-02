square = [
    ["0010",
     "1111",
     "0010"],
    ["0100",
     "1111",
     "1000"],
    ["0010",
     "1111",
     "0100"],
    ["0001",
     "1111",
     "1000"],
    ["0001",
     "1111",
     "0100"],
    ["11100",
     "00111"],
    ["1100",
     "0111",
     "0010"],
    ["1100",
     "0111",
     "0001"],
    ["0010",
     "1110",
     "0011"],
    ["0001",
     "1111",
     "0001"],
    ["1100",
     "0110",
     "0011"]
]
def mirror(b): # 대칭
    ans = []
    for i in range(len(b)):
        temp = b[i][::-1]
        ans.append(temp)
    return ans
def rotate(b): # 회전시키기. 시계방향으로
    ans = ['']*len(b[0])
    for j in range(len(b[0])):
        for i in range(len(b)-1, -1, -1):
            ans[j] += b[i][j]
    return ans

# 전개도에 해당하는지 확인
def check(a, b, x, y): # a : 입력받은 배열    b : 비교할 전개도    x : 전개도랑 비교할 현재 위치 행    y : 전개도랑 비교할 현재 위치 열
    n = len(a)
    for i in range(len(b)):
        for j in range(len(b[0])):
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < n:
                if b[i][j] == '0':
                    if a[nx][ny] == 1:
                        return False
                elif b[i][j] == '1':
                    if a[nx][ny] == 0:
                        return False
            else:
                return False
    return True
T = 3
for _ in range(T):
    n = 6
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = False
    for c in square:
        cube = [row[:] for row in c]
        for mir in range(2):
            for rot in range(4):
                for i in range(n):
                    for j in range(n):
                        ans |= check(a, cube, i, j)
                cube = rotate(cube)
            cube = mirror(cube)
    if ans:
        print("yes")
    else:
        print("no")