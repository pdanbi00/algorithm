# 맨 마지막 집부터 방문하면서 방문할 때 모든 배달과 수거가 0이 되도록

def solution(cap, n, deliveries, pickups):
  answer = 0
  deliver = 0   # 남은 배달 가능 개수
  pick = 0   # 남은 수거 가능 개수
  for i in range(n-1, -1, -1):
    cnt = 0
    while deliver < deliveries[i] or pick < pickups[i]:
      cnt += 1
      deliver += cap
      pick += cap
    deliver -= deliveries[i]
    pick -= pickups[i]
    answer += (i + 1) * cnt
  return answer * 2