import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
limit = int(input())
money.sort()

# 이분탐색 삘
if sum(money) <= limit:
    print(max(money))
else:
    start = 0
    end = limit
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in range(len(money)):
            if money[i] <= mid:
                total += money[i]
            else:
                total += mid * (len(money) - i)
                break
        if total <= limit:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)