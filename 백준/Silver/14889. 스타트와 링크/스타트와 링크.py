# 조합으로 팀 나누기
# 각 팀별로 능력치 구하기
# 능력치 차이 최소 답으로
def solve(n, r, s):
    global min_v

    if r == 0:
        start_total = 0
        link_total = 0
        idx = 0
        for n in num:
            if n not in team_start:
                team_link[idx] = n
                idx += 1

        for i in range((N // 2) - 1):
            for j in range(i + 1, N // 2):
                start_total += board[team_start[i]][team_start[j]]
                start_total += board[team_start[j]][team_start[i]]
                link_total += board[team_link[i]][team_link[j]]
                link_total += board[team_link[j]][team_link[i]]

        ans = abs(start_total - link_total)
        if ans < min_v:
            min_v = ans
        return
    else:
        for i in range(s, n-r+1):
            team_start[N//2 - r] = num[i]
            solve(n, r-1, i+1)

N = int(input())
board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
min_v = 100 * N
num = [x for x in range(1, N+1)]
team_start = [0] * (N//2)
team_link = [0] * (N//2)
solve(N, N//2, 0)

print(min_v)