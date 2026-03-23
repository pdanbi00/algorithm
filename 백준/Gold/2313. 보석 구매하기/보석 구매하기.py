N = int(input())
total = 0
ans_idx = []
for _ in range(N):
    L = int(input())
    jewerly = list(map(int, input().split()))

    # 연속된 보석의 합은 누적합으로 저장
    # 보석의 가치가 음수일 경우도 있기 때문에
    sum = []
    for i in range(L):
        if i == 0:
            sum.append((1, jewerly[i]))
        else:
            # 이전 누적을 이어가는 경우
            if sum[i-1][1] + jewerly[i] > jewerly[i]:
                sum.append((sum[i-1][0] + 1, sum[i-1][1] + jewerly[i]))
            else:
                sum.append((1, jewerly[i]))

    # 최대 구간 찾기
    idx = 0
    cnt = sum[0][0]
    max_sum = sum[0][1]

    for j in range(1, L):
        if sum[j][1] >= max_sum:
            if sum[j][1] == max_sum and sum[j][0] >= cnt:
                continue
            idx = j
            cnt = sum[j][0]
            max_sum = sum[j][1]

    total += max_sum
    ans_idx.append((idx + 1 - cnt + 1, idx + 1))

print(total)
for s, e in ans_idx:
    print(s, e)