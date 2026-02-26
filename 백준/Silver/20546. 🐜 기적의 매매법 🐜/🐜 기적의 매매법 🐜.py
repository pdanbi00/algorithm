money = int(input())

stock = list(map(int, input().split()))

J, S = money, money # 현금
stock_j, stock_s = 0, 0 # 주식

# 준현이
for i in range(14):
    if stock[i] <= J:
        stock_j += J // stock[i]
        J = J % stock[i]
J += stock_j * stock[13]

# 성민이
for i in range(4, 14):
    # 3일 연속 상승인지 확인
    cnt = 0
    for j in range(3, 0, -1):
        if stock[i-j] < stock[i-j+1]:
            cnt += 1
    if cnt == 3:
        if stock_s > 0:
            S += stock[i] * stock_s
            stock_s = 0

    # 3일 연속 하락인지 확인
    cnt = 0
    for j in range(3, 0, -1):
        if stock[i - j] > stock[i - j + 1]:
            cnt += 1
    if cnt == 3:
        if S > 0:
            stock_s += S // stock[i]
            S = S % stock[i]

S += stock_s * stock[13]

if S > J:
    print("TIMING")
elif S == J:
    print("SAMESAME")
else:
    print("BNP")