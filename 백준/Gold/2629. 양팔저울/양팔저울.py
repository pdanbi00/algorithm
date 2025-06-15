N = int(input())
chu = list(map(int, input().split()))

dp = [False] * 15001
for c in chu:
    arr = []
    for i in range(15001):
        if dp[i]:
            arr.append(i)

    for a in arr:
        if a - c >= 0:
            # print(a, a-c)
            dp[a-c] = True

        if c - a >= 0:
            # print(a, c-a)
            dp[c-a] = True

        if a + c <= 15000:
            # print(a, a+c)
            dp[a+c] = True
    dp[c] = True

goosle = int(input())
goosles = list(map(int, input().split()))

for goo in goosles:
    if goo <= 15000:
        if dp[goo]:
            print('Y', end = " ")
        else:
            print('N', end = " ")
    else:
        print('N', end = " ")