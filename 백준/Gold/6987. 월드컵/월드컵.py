# 모든 경기는 승무패의 개수가 정해져 있기 때문에 15개 경기까지 조합을 미리 구하고 dfs 돌리면서 승무패 1씩 빼면서 전체 합계가 0이 될 수 있는지 확인
from itertools import combinations

# 백트래킹
def dfs(round):
    global ans
    if round == 15:
        ans = 1
        for sub in result:
            if sub.count(0) != 3:
                ans = 0
                break
        return

    t1, t2 = game[round] # 대결할 나라 선정
    for x, y in ((0, 2), (1, 1), (2, 0)): # x가 이기고, 비기고, x가 지는 상황
        if result[t1][x] > 0 and result[t2][y] > 0:
            result[t1][x] -= 1
            result[t2][y] -= 1
            dfs(round+1)
            result[t1][x] += 1
            result[t2][y] += 1

answer = []
game = list(combinations(range(6), 2))
for i in range(4):
    data = list(map(int, input().split()))
    result = [data[j:j+3] for j in range(0, 16, 3)]
    ans = 0
    dfs(0)
    answer.append(ans)
print(*answer)