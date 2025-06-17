# 피자의 크기보다 작거나 마지막일 경우 그 위치에 고정됨. 그 위치는 이제 막혔다고 표시
D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 1. oven 재정렬. 이전 오븐 기준으로 그거보다 큰 도우는 들어갈 수 없음
# ex) 5 6 4 3 6 2 3 -> 5 5 4 3 3 2 2
for i in range(len(oven)-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

# 반죽 넣기
result = 0
oven_idx = len(oven) - 1
break_cnt = 0

for p in pizza:
    # 1. 오븐 크기만큼 순회
    while oven_idx >= 0:
        # 2. 지금 오븐의 크기보다 피자의 크기가 작으면 동톼
        if p <= oven[oven_idx]:
            result = oven_idx
            oven_idx -= 1
            break_cnt += 1
            break
        else:
            oven_idx -= 1

if break_cnt == N:
    print(result+1)
else:
    print(0)