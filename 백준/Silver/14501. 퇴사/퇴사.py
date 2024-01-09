n = int(input())
arr = [(0,0)]
dp = [0 for _ in range(n+1)]

for _ in range(1, n+1) :
  t,p = map(int, input().split())
  arr.append((t,p))

for i in range(1, n+1) :
  time = arr[i][0]
  money = arr[i][1]
  if i+time > n+1 : # 상담이 n일전에 끝나지 않는다면 
    continue
  else :
    dp[i] = max(dp[i], money)
    for j in range(i+time, n+1) :
      next_time = arr[j][0]
      if j + next_time <= n+1 :
        dp[j] = max(dp[j], arr[j][1]+dp[i])
    

print(max(dp))