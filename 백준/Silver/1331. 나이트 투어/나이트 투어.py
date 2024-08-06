# 조건 1 : 나이트의 이동 규칙을 지켜야 함. (r, c) 절댓값 차이가 (2, 1) 혹은 (1, 2)이어야 됨
# 조건 2 : 재방문 불가
# 조건 3 : 마지막 칸에서 시작 지점으로 돌아올 수 있어야한다. 즉, 마지막 칸이랑 시작점도 절댓값 차이가 (1, 2) 혹은 (2, 1) 이어야 됨.

possbile = True
visited = [[False] * 6 for _ in range(6)]

alpha = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def check(before, move):
    before_num = alpha[before[0]]
    move_num = alpha[move[0]]

    # 절댓값 차이랑 재방문 여부 확인
    if abs(before_num - move_num) == 2 and abs(int(before[1]) - int(move[1])) == 1 and not visited[move_num][int(move[1]) - 1]:
        visited[move_num][int(move[1]) - 1] = True
    elif abs(before_num - move_num) == 1 and abs(int(before[1]) - int(move[1])) == 2 and not visited[move_num][int(move[1]) - 1]:
        visited[move_num][int(move[1]) - 1] = True
    else:
        return False
    return True

for i in range(36):
    move = input()
    if i == 0:
        start = move
    else:
        if not check(before, move):
            possbile = False
            break
    before = move

# 조건 3에 부합하는지
if not check(move, start):
    possbile = False
if possbile:
    print('Valid')
else:
    print('Invalid')