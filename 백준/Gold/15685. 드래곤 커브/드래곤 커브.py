dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
dragon_curve = [[False] * 101 for _ in range(101)]

# 드래곤 커브 만들기
def curve(x, y, dir, gen):
    ans = [dir]
    for g in range(1, gen+1):
        temp = ans[:]
        temp.reverse()
        # 문제에는 90도 시계 방향 회전 시키라 했지만
        # 실제로 그려보면 반시계 방향 회전 한거임
        # 마침 dr, dc 순서가 옆에꺼 반시계방향으로 돌린거라서
        for i in range(len(temp)):
            temp[i] = (temp[i]+1) % 4
        ans += temp
    return ans

N = int(input())
for _ in range(N):
    c, r, d, g = map(int, input().split())
    dirs = curve(r, c, d, g)
    dragon_curve[r][c] = True
    for dir in dirs:
        r += dr[dir]
        c += dc[dir]
        dragon_curve[r][c] = True
ans = 0
for i in range(100): # 격자는 0번 부터 101번까지 있지만 1x1 정사각형 보려면 100, 100까지만 보면 되니깐 범위가 100까지
    for j in range(100):
        if dragon_curve[i][j] and dragon_curve[i][j+1] and dragon_curve[i+1][j+1] and dragon_curve[i+1][j]:
            ans += 1
print(ans)