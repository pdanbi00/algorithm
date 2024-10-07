N = int(input())
balls = list(input())

# R 개수 세기, B 개수 세기
# 제일 왼쪽부터 R 연속인거 개수, B 연속인거 개수, 제일 오른쪽에서부터 R연속인거 개수, B연속인거 개수

r_cnt = 0
b_cnt = 0
for i in range(N):
    if balls[i] == 'R':
        r_cnt += 1
    else:
        b_cnt += 1
answer = min(r_cnt, b_cnt)

# 앞에서부터 연속된 구간 확인하기
cnt = 0
for i in range(N):
    if balls[i] != balls[0]:
        break
    cnt += 1

if balls[0] == 'R':
    answer = min(answer, r_cnt - cnt)
else:
    answer = min(answer, b_cnt - cnt)

# 뒤에서부터 연속된 구간 확인하기
cnt = 0
for i in range(N-1, -1, -1):
    if balls[i] != balls[-1]:
        break
    cnt += 1

if balls[-1] == 'R':
    answer = min(answer, r_cnt - cnt)
else:
    answer = min(answer, b_cnt - cnt)

print(answer)