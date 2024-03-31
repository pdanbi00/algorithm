import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
ans = 1e9
house = [] # 집 좌표
chick = [] # 치킨집 좌표

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chick.append((i, j))

for chi in combinations(chick, M): # m개의 치킨집 선택
    temp = 0
    for h in house:
        chi_len = 1e9 # 각 집에서 치킨집까지의 거리
        for c in chi:
            chi_len = min(chi_len, abs(c[0]-h[0])+abs(c[1]-h[1]))
        temp += chi_len
    if temp < ans:
        ans = temp
print(ans)