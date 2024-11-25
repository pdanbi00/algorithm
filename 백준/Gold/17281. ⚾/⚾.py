from itertools import permutations
N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

# 조건
# 1. 한 이닝에 3아웃 발생하면 이닝 종료
# 2. 9번 타자까지 쳤는데 3아웃이 발생 안했으면 이닝 종료 안함.
# 3. 1번 이닝에서 6번 타자가 마지막이면 2번 이닝은 7번 타자부터 시작
# 4. 경기 시작하기 전에 타순 정해주기, 4번 타자는 1번 선수로 고정
order = [i for i in range(1, 9)]
ans = 0
for perm in permutations(order, 8):
    perm = list(perm)
    batter = perm[:3] + [0] + perm[3:]
    idx, score = 0, 0 # 몇번째 선수인지, 몇점인지
    for i in range(N): # 각 이닝
        out = 0
        p1, p2, p3 = 0, 0, 0 # 1루 ~ 3루 상태
        while out < 3:
            if innings[i][batter[idx]] == 0:
                out += 1
            elif innings[i][batter[idx]] == 1:
                score += p3
                p1, p2, p3 = 1, p1, p2
            elif innings[i][batter[idx]] == 2:
                score += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif innings[i][batter[idx]] == 3:
                score += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif innings[i][batter[idx]] == 4:
                score += p1 + p2 + p3 + 1
                p1, p2, p3 = 0, 0, 0
            idx += 1
            if idx == 9:
                idx = 0
    ans = max(ans, score)
print(ans)
