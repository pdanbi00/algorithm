N = int(input())
cards = list(map(int, input().split()))
M = int(input())
min_cost = min(cards)
# 제일 긴 자리수 결정
nums = []
for i in range(N):
    cnt = M // cards[i]
    nums.append([cnt, i])
nums.sort(key=lambda x: x[0], reverse=True)
ans = []
cost = 0
# 제일 많이 살 수 있는 수가 0 이면 그 다음으로 많이 살 수 있는 수를 제일 앞에 넣고 나머지 다 0으로 채우기
if nums[0][1] == 0:
    if N >= 2 and cards[nums[1][1]] <= M:
        ans.append(nums[1][1])
        cost += cards[nums[1][1]]
    else:
        print(0)
        exit()
while cost + cards[nums[0][1]] <= M:
    ans.append(nums[0][1])
    cost += cards[nums[0][1]]

# 자리수 결정 다 했으면 앞에서부터 큰 숫자로 교체
for i in range(len(ans)):
    for j in range(N-1, -1, -1):
        if cost - cards[ans[i]] + cards[j] <= M:
            cost = cost - cards[ans[i]] + cards[j]
            ans[i] = j
            break
for i in ans:
    print(i, end='')
