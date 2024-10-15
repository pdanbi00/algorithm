N = int(input())
bildings = list(map(int, input().split()))

cnt = [0] * (N+1) # i번째 건물이 볼 수 있는 건물 수
near = [[int(1e9), int(1e9)] for _ in range(N+1)] # 가장 가까운 건물 번호, 가장 가까운 건물 거리

# 앞에서부터 진행 : 왼쪽에서 볼 수 있는 건물
stack = []
for idx, v in enumerate(bildings, 1):
    # stack pop 조건 : 데이터가 있고, 스택 제일 위 건물의 높이가 현재 건물의 높이와 같거나 작으면 더이상 안보여서 pop
    while stack and stack[-1][1] <= v:
        stack.pop()
    cnt[idx] += len(stack)

    if stack:
        dist = abs(stack[-1][0] - idx) # 해당 건물 기준 가장 가까운 좌측 건물과의 거리
        if dist < near[idx][1]:
            near[idx][0] = stack[-1][0]
            near[idx][1] = dist
        elif dist == near[idx][1] and stack[-1][0] < near[idx][0]: #  거리는 같은데 건물번호가 더 작은 경우
            near[idx][0] = stack[-1][0]
    stack.append((idx, v))

# 뒤에서부터 진행 : 오른쪽에서 볼 수 있는 건물
stack = []
for idx, v in reversed(list(enumerate(bildings, 1))):
    # stack pop 조건 : 데이터가 있고, 스택 제일 위 건물의 높이가 현재 건물의 높이와 같거나 작으면 더이상 안보여서 pop
    while stack and stack[-1][1] <= v:
        stack.pop()
    cnt[idx] += len(stack)

    if stack:
        dist = abs(stack[-1][0] - idx) # 해당 건물 기준 가장 가까운 좌측 건물과의 거리
        if dist < near[idx][1]:
            near[idx][0] = stack[-1][0]
            near[idx][1] = dist
        elif dist == near[idx][1] and stack[-1][0] < near[idx][0]: #  거리는 같은데 건물번호가 더 작은 경우
            near[idx][0] = stack[-1][0]
    stack.append((idx, v))
# 최종 결과 출력
for i in range(1, N+1):
    if cnt[i] > 0:
        print(cnt[i], near[i][0])
    else:
        print(0)