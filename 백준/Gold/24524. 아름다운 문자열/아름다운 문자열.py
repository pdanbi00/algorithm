S = input()
T = input()

dp = [0] * (len(T) + 1)

dp[0] = 1e9

find_idx = dict()

for i in range(len(T)):
    find_idx[T[i]] = i+1

for s in S:
    if s in find_idx and dp[find_idx[s]-1] > dp[find_idx[s]]:
        dp[find_idx[s]] += 1

print(dp[-1])