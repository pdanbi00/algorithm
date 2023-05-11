T = int(input())
DP = [0] * 12
DP[1] = 1 # 1
DP[2] = 2 # 1 + 1 , 2
DP[3] = 4 # 1 + 1 + 1, 2 + 1, 1 + 2, 3
for i in range(4, 12):
    DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
for _ in range(T):
    n = int(input())
    print(DP[n])