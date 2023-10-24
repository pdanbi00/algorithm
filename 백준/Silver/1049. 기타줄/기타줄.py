N, M = map(int, input().split())
money = 100000
min_package = 1000
min_one = 1000
for i in range(M):
    package, one = map(int, input().split())
    if min_package > package:
        min_package = package
    if min_one > one:
        min_one = one
money = min(money, min_package * ((N // 6) + 1), (min_package * (N // 6)) + (min_one * (N % 6)), min_one * N)
print(money)