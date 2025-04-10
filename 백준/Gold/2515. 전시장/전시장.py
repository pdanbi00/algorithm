import sys
input = sys.stdin.readline

N, S = map(int, input().split())
heights = []
prices = {}
for _ in range(N):
    h, p = map(int, input().split())
    if h < S:
        continue
    if h in prices:
        prices[h] = max(prices[h], p)
    else:
        prices[h] = p
        heights.append(h)

heights.sort()

# 높이가 x보다 작거나 같은 그림 중 가장 큰 그림의 가격 찾기
def find(x):
    start = 0
    end = len(heights)
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if heights[mid] <= x:
            start = mid + 1
            res = prices[heights[mid]]
        else:
            end = mid - 1

    return res

for i, l in enumerate(heights):
    # l - s 이하 중 가장 큰 그림 찾기
    if i == 0:
        continue
    prices[l] = max(prices[heights[i-1]], find(l-S) + prices[l])
print(prices[l])