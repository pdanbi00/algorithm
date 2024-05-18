# DP문제임..
# dp[i][j] : 알고력 i, 코딩력 j에 도달하는데 걸리는 최단 시간
def solution(alp, cop, problems):
    max_alp_req = 0
    max_cop_req = 0
    
    # 목표 알고력, 코딩력 찾기
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
        
    # 둘 중 하나라도 목표값 넘어가면 안됨. dp 기록 못해서 그러는듯
    alp = min(alp, max_alp_req) 
    cop = min(cop, max_cop_req)
    
    dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    
    dp[alp][cop] = 0 # 지금 가지고 있는 기본 알고력, 코딩력
    
    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
                
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    # 이거도 둘 중 한개라도 목표 넘기면 안됨.
                    new_alp = min(i+alp_rwd, max_alp_req)
                    new_cop = min(j+cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j]+cost)
        
        
        
    return dp[max_alp_req][max_cop_req]