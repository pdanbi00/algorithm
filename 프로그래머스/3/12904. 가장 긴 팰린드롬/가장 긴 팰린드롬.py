# def solution(s):
#     answer = 1
    
#     N = len(s)
#     dp = [[0] * N for _ in range(N)]
#     for i in range(N):
#         dp[i][i] = 1
        
#     for i in range(N-1):
#         if (s[i] == s[i+1]):
#             dp[i][i+1] = 1
#             answer = 2
            
#     for k in range(2, N):
#         for i in range(N-k):
#             j = i + k
#             if (s[i] == s[j] and dp[i+1][j-1] == 1):
#                 dp[i][j] = 1
#                 answer = max(answer, j - i + 1)

#     return answer


def solution(s):
    answer = 0
    
    N = len(s)
    
    for k in range(N, 0, -1):
        for i in range(N-k+1):
            start = i
            end = i + k - 1
            flag = True
            
            while (start <= end):
                if (s[start] != s[end]):
                    flag = False
                    break
                    
                start += 1
                end -= 1
            
            if flag:
                return k

    return answer