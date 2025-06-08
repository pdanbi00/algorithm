R, C = map(int, input().split())
board = []
arduino = []

for i in range(R):
    arr = list(input())
    for j in range(C):
        if arr[j] == 'R':
            arduino.append([i, j])
        elif arr[j] == 'I':
            j_r, j_c = i, j
    board.append(arr)
dirs = list(input())

dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

adr = [1, 1, 1, 0, 0, -1, -1, -1]
adc = [-1, 0, 1, -1, 1, -1, 0, 1]

idx = 0

def amove(ar, ac):
    min_dis = 1e9
    min_r, min_c = -1, -1
    for k in range(8):
        anr = ar + adr[k]
        anc = ac + adc[k]
        if 0 <= anr < R and 0 <= anc < C:
            dis = abs(anr - j_r) + abs(anc - j_c)
            if dis < min_dis:
                min_dis = dis
                min_r = anr
                min_c = anc
    return (min_r, min_c)

while idx < len(dirs):
    # 1. 종수 이동시키기
    j_r += dr[int(dirs[idx])-1]
    j_c += dc[int(dirs[idx])-1]

    # 2. 종수가 아두이노 있는 칸으로 이동했는지 확인
    if (j_r, j_c) in arduino:
        print("kraj", idx+1)
        exit()

    # 3. 아두이노 이동시키기
    arduino_set = set()
    arduino_dict = dict()
    for i in range(len(arduino)):
        tmp = amove(arduino[i][0], arduino[i][1])
        if tmp in arduino_dict:
            arduino_dict[tmp] += 1
        else:
            arduino_dict[tmp] = 1

        arduino_set.add(tmp)
        # 종수 있는 곳으로 아두이노가 이동했다면 게임 중지
        if tmp[0] == j_r and tmp[1] == j_c:
            print("kraj", idx + 1)
            exit()

    # 같은 칸에 아두이노 몇개 있는지 확인하고 없애기
    for k, v in arduino_dict.items():
        if v >= 2:
            arduino_set.remove(k)

    arduino = list(arduino_set)

    idx += 1

board = [['.'] * C for _ in range(R)]
board[j_r][j_c] = 'I'
for r, c in arduino:
    board[r][c] = 'R'

for i in range(R):
    print(''.join(board[i]))

'''
8 8
........
....R...
........
.......R
........
........
....I...
.......R
778524


kraj 3
'''