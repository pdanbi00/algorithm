N = int(input())
board = [list(input()) for _ in range(5)]

light = """###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###""".split()
# 전구 위치에 따라서 만들 수 있는 숫자 후보
can_make = {}

def make_light():
    for i in range(5):
        for j in range(3):
            can_make[(i, j)] = set()
            # 만들 수 있는 숫자 찾기
            for k in range(10):
                if light[i][j+k*4] == '#':
                    can_make[(i, j)].add(k)

make_light()
ans = 0.0
for s in range(N):
    tmp = set(range(10)) # 처음에는 모든 숫자를 만들 수 있다고 가정
    for i in range(5):
        for j in range(s*4, s*4 + 3):
            if board[i][j] == "#":
                tmp &= can_make[(i, j % 4)] # 그 전구가 켜졌을 때 만들 수 있는 숫자와 교집합을 구함

    # 숫자 평군 구해서 더하기
    if tmp:
        ans *= 10
        ans += sum(tmp) / len(tmp)
    else:
        ans = -1
        break # 하나라도 후보가 되는 수가 없으면 불가능

print(ans)