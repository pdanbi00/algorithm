T = int(input())
for _ in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    team_cnt = max(scores)
    possible = []
    # 6명이 경기 뛴 팀 뽑아내기
    for i in range(1, team_cnt+1):
        if scores.count(i) == 6:
            possible.append(i)
    score = [[] for _ in range(team_cnt + 1)]
    s = 1
    for i in range(N):
        if scores[i] in possible:
            score[scores[i]].append(s)
            s += 1
    answer = 0
    min_total = 1e9
    min_five = 1e9
    for i in range(len(score)):
        if len(score[i]) > 0:
            if min_total > sum(score[i][:4]):
                min_total = sum(score[i][:4])
                min_five = score[i][4]
                answer = i
            elif min_total == sum(score[i][:4]):
                if score[i][4] < min_five:
                    min_five = score[i][4]
                    answer = i

    print(answer)