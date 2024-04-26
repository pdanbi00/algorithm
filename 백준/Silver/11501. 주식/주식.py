import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    price.reverse()
    maxPrice = 0 # 주식 최대 가격
    sum = 0 # 주식으로 벌 수 있는 최대 수익
    for i in range(N):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else:
            sum += maxPrice - price[i]
    print(sum)