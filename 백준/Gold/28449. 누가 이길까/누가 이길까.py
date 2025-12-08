N, M = map(int, input().split())
HI = list(map(int, input().split()))
ARC = list(map(int, input().split()))

HI_score = [0] * 100001
for i in range(N):
    HI_score[HI[i]] += 1

for i in range(1, 100001):
    HI_score[i] += HI_score[i-1]

win = 0
lose = 0
draw = 0

for s in ARC:
    win += N - HI_score[s]
    lose += HI_score[s-1]
    draw += HI_score[s] - HI_score[s-1]

print(win, lose, draw)