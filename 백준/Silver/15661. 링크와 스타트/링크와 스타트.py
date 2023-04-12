def solve(n, r, s):
    global min_v

    if r == 0:
        start_total = 0
        link_total = 0
        idx = 0
        for num in nums:
            if num not in team_start:
                team_link[idx] = num
                idx += 1

        # 각 팀별로 능력치 구하기
        # 첫번째 두번째, 첫번째 세번째 ... 이런식으로 능력치 구함
        # 두번째 첫번째 이렇게도 구해야됨.
        # 한 팀에 1명만 있을 경우랑 2명이상일 경우랑 나눔
        # 왜냐하면 한명일 경우에 len()-1 하면 0이라서 for문을 돌 수 가 없어서
        # if len(team_start) == 1:
        #     start_total = 0
        #     cnt = 0
        #     for i in range(len(team_link)-1):
        #         for j in range(i + 1, len(team_link)):
        #             link_total += board[team_link[i]][team_link[j]]
        #             link_total += board[team_link[j]][team_link[i]]

        # else:
        for i in range(len(team_start) - 1):
            for j in range(i + 1, len(team_start)):
                start_total += board[team_start[i]][team_start[j]]
                start_total += board[team_start[j]][team_start[i]]
        for i in range(len(team_link) - 1):
            for j in range(i + 1, len(team_link)):
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
            team_start[length - r] = nums[i]
            solve(n, r-1, i+1)

N = int(input())
board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
min_v = 100 * N
nums = [x for x in range(1, N+1)]
for l in range(1, (N//2) + 1):
    length = l
    team_start = [0] * length
    team_link = [0] * (N - length)
    solve(N, length, 0)
print(min_v)