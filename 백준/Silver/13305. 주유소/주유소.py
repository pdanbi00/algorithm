N = int(input())

distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_price = 1e9
total = 0
for i in range(N-1):
    if oil[i] < min_price:
        min_price = oil[i]
    total += distance[i] * min_price

print(total)