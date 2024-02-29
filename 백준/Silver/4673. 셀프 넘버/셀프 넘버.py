dp = [0] * 10001
for i in range(1, 10001):
    num = str(i)
    n = int(num)
    for j in range(len(num)):
        n += int(num[j])
    if n <= 10000:
        dp[n] = i
for i in range(1, 10001):
    if dp[i] == 0:
        print(i)