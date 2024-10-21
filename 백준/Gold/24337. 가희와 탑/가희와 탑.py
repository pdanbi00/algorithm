# 우선 건물 수 N은 고려하지 않음
# 왼쪽부터 건물이 1부터 a까지 오름차순, 그 옆으로는 b부터 1까지 내림차순
# a와 b 중에 더 낮은 높이의 건물은 존재하면 안됨.
# -> a = 3, b = 2인 경우 1 2 3 2 1 이 아니라 1 2 3 1 이어야 한
# 즉, 1 ~ (a-1)까지 건물 세우고, max(a, b) 높이 건물 세우고, (b-1) ~ 1까지 건물세움
N, a, b = map(int, input().split())
answer = []
# N 고려 안하고 제일 간단하게 조건 만족시키기
for i in range(1, a):
    answer.append(i)
answer.append(max(a, b))
for i in range(b-1, 0, -1):
    answer.append(i)

if len(answer) > N:
    print(-1)
else:
    print(answer[0], end = " ")
    for i in range(N-len(answer)):
        print(1, end = " ")
    for i in range(1, len(answer)):
        print(answer[i], end = " ")