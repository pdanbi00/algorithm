# 조합으로 팀 나누기
# N명이니까 1부터 N까지 중에 N//2개 선택
# 다 뽑으면 팀은 다 짜진거니까 팀별 능력치를 구해봄
# 각 팀별 능력치 다 구하면
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

        # 각 팀별로 능력치 구하기
        # 첫번째 두번째, 첫번째 세번째 ... 이런식으로 능력치 구함
        # 두번째 첫번째 이렇게도 구해야됨.
        for i in range((N // 2) - 1):
            for j in range(i + 1, N // 2):
                start_total += board[team_start[i]][team_start[j]]
                start_total += board[team_start[j]][team_start[i]]
                link_total += board[team_link[i]][team_link[j]]
                link_total += board[team_link[j]][team_link[i]]
        # 팀별 능력치 차이 구함
        ans = abs(start_total - link_total)
        # 구한 능력치 차이가 지금껏 나온 최소 능력치 차이보다 작으면 값 갱시
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