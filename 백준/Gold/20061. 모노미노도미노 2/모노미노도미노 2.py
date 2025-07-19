import sys
input = sys.stdin.readline
N = int(input())
blueBoard = [[0] * 6 for _ in range(4)]
greenBoard = [[0] * 4 for _ in range(6)]
score = 0

def blue(t, x, y):
    global score
    # 1. 블럭 쌓기. 블럭 들어오는 행은 고정. 열 확인하기
    if t == 1: # 1 x 1 블럭일 경우
        idx = -1
        for j in range(6):
            # 채워져 있는 칸 바로 앞에 넣기
            if blueBoard[x][j] == 1:
                idx = j-1
                break
        if idx == -1:
            blueBoard[x][5] = 1
        else:
            blueBoard[x][idx] = 1
    elif t == 2: # 1 x 2 블럭일 경우(가로로 긴 경우) (x, y), (x, y+1) 채우기
        idx = -1
        for j in range(6):
            # 채워져 있는 칸 바로 앞에 넣기
            if blueBoard[x][j] == 1:
                idx = j - 2
                break
        if idx == -1:
            blueBoard[x][5] = 1
            blueBoard[x][4] = 1
        else:
            blueBoard[x][idx] = 1
            blueBoard[x][idx+1] = 1
    elif t == 3: # 2 x 1 블럭일 경우(세로로 긴 경우) (x, y), (x+1, y)
        # 두 행 중 먼저 튀어 나온 곳 기준으로
        idx = -1
        for j in range(6):
            # 채워져 있는 칸 바로 앞에 넣기
            if blueBoard[x][j] == 1 or blueBoard[x+1][j] == 1:
                idx = j - 1
                break
        if idx == -1:
            blueBoard[x][5] = 1
            blueBoard[x+1][5] = 1
        else:
            blueBoard[x][idx] = 1
            blueBoard[x+1][idx] = 1

    # 2. 가득찬 열 있는지 확인하기
    fullCol = []
    for j in range(6):
        cnt = 0
        for i in range(4):
            if blueBoard[i][j] == 1:
                cnt += 1
        if cnt == 4:
            fullCol.append(j)
            score += 1

    if fullCol:
        # 해당 열들 다 빈칸으로 만들기
        for j in range(len(fullCol)):
            for i in range(4):
                blueBoard[i][fullCol[j]] = 0
        # 해당 열들 왼쪽에 있는 블럭들 가득찼던 열 개수만큼 오른쪽으로 옮기기
        idx = fullCol[0] # 이게 가장 왼쪽에 위치한 열이니깐 이 열보다 앞에 있는 열들 옮겨주기
        for j in range(idx-1, -1, -1):
            for i in range(4):
                blueBoard[i][j+len(fullCol)] = blueBoard[i][j]
                blueBoard[i][j] = 0

    # 3. 0열 혹은 1열에 블럭 있는지 확인하기
    zeroCol = []
    for j in range(2):
        for i in range(4):
            if blueBoard[i][j] == 1:
                zeroCol.append(j)
                break
    if zeroCol:
        # 0열 혹은 1열 중에 블럭 있는 열 개수 만큼 오른쪽부터 없애기
        for k in range(len(zeroCol)):
            for i in range(4):
                blueBoard[i][5-k] = 0
        # 나머지 열들 없앤 열 수 만큼 오른쪽으로 옮기기
        for j in range(5-len(zeroCol), -1, -1):
            for i in range(4):
                blueBoard[i][j+len(zeroCol)] = blueBoard[i][j]
                blueBoard[i][j] = 0
        # 0열 혹은 1열 블럭 빈칸으로 만들기
        for k in range(len(zeroCol)):
            for i in range(4):
                blueBoard[i][1-k] = 0

def green(t, x, y):
    global score
    # 1. 블럭 쌓기. 블럭 들어오는 열은 고정. 행 확인하기
    if t == 1: # 1 x 1 블럭일 경우
        idx = -1
        for i in range(6):
            # 채워져 있는 칸 바로 앞에 넣기
            if greenBoard[i][y] == 1:
                idx = i-1
                break
        if idx == -1:
            greenBoard[5][y] = 1
        else:
            greenBoard[idx][y] = 1
    elif t == 2: # 1 x 2 블럭일 경우(가로로 긴 경우) (x, y), (x, y+1) 채우기
        # 두 행 중 먼저 튀어 나온 곳 기준으로
        idx = -1
        for i in range(6):
            # 채워져 있는 칸 바로 앞에 넣기
            if greenBoard[i][y] == 1 or greenBoard[i][y + 1] == 1:
                idx = i - 1
                break
        if idx == -1:
            greenBoard[5][y] = 1
            greenBoard[5][y + 1] = 1
        else:
            greenBoard[idx][y] = 1
            greenBoard[idx][y + 1] = 1

    elif t == 3: # 2 x 1 블럭일 경우(세로로 긴 경우) (x, y), (x+1, y)
        idx = -1
        for i in range(6):
            # 채워져 있는 칸 바로 앞에 넣기
            if greenBoard[i][y] == 1:
                idx = i - 2
                break
        if idx == -1:
            greenBoard[5][y] = 1
            greenBoard[4][y] = 1
        else:
            greenBoard[idx][y] = 1
            greenBoard[idx + 1][y] = 1

    # 2. 가득찬 행 있는지 확인하기
    fullRow = []
    for i in range(6):
        cnt = 0
        for j in range(4):
            if greenBoard[i][j] == 1:
                cnt += 1
        if cnt == 4:
            fullRow.append(i)
            score += 1

    if fullRow:
        # 해당 행들 다 빈칸으로 만들기
        for i in range(len(fullRow)):
            for j in range(4):
                greenBoard[fullRow[i]][j] = 0
        # 해당 열들 왼쪽에 있는 블럭들 가득찼던 열 개수만큼 오른쪽으로 옮기기
        idx = fullRow[0] # 이게 가장 왼쪽에 위치한 열이니깐 이 열보다 앞에 있는 열들 옮겨주기
        for i in range(idx-1, -1, -1):
            for j in range(4):
                greenBoard[i+len(fullRow)][j] = greenBoard[i][j]
                greenBoard[i][j] = 0

    # 3. 0열 혹은 1열에 블럭 있는지 확인하기
    zeroRow = []
    for i in range(2):
        for j in range(4):
            if greenBoard[i][j] == 1:
                zeroRow.append(i)
                break
    if zeroRow:
        # 0행 혹은 1행 중에 블럭 있는 행 개수 만큼 아래쪽부터 없애기
        for k in range(len(zeroRow)):
            for j in range(4):
                greenBoard[5-k][j] = 0
        # 나머지 행들 없앤 행 수 만큼 아래쪽부터 옮기기
        for i in range(5-len(zeroRow), -1, -1):
            for j in range(4):
                greenBoard[i+len(zeroRow)][j] = greenBoard[i][j]
                greenBoard[i][j] = 0
        # 0행 혹은 1행 블럭 빈칸으로 만들기
        for k in range(len(zeroRow)):
            for j in range(4):
                greenBoard[1-k][j] = 0

for _ in range(N):
    t, x, y = map(int, input().split())
    blue(t, x, y)
    green(t, x, y)

print(score)
cnt = 0
for i in range(6):
    for j in range(4):
        if blueBoard[j][i] == 1:
            cnt += 1
        if greenBoard[i][j] == 1:
            cnt += 1
print(cnt)