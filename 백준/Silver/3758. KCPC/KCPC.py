import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    scores = [[0] * (k+1) for _ in range(n+1)]
    time = [0] * (n+1) # 제출 시간
    cnt = [0] * (n+1) # 제출 횟수
    for i in range(m):
        ID, problem, score = map(int, input().split())
        if scores[ID][problem] == 0:
            scores[ID][problem] = score
        else:
            if score > scores[ID][problem]:
                scores[ID][problem] = score
        time[ID] = i
        cnt[ID] += 1
    # print(scores)
    final_score = []
    for i in range(n+1):
        final_score.append((sum(scores[i]), cnt[i], time[i], i))
    # print(final_score)
    final_score.sort(key=lambda x : (x[0], -x[1], -x[2]), reverse=True)
    answer = 0
    for i in range(n+1):
        if final_score[i][3] == t:
            print(answer+1)
            break
        answer += 1

