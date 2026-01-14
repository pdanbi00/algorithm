N, K = map(int, input().split())

# dp[N][M] : 길이가 N이고 문자열의 뒷부분 상태가 M인 안전한 암호의 개수
# M은 0 ~ 6 중 하나
'''
1 : A
2 : AB
3 : ABC -> 4 : ABCB -> ABCBC 불가능
5 : ABA -> 6 : ABAB -> ABABC 불가능
0 : 1 ~ 6 어느 것에도 해당하지 않는 경우

현재 상태 | 다음 상태
    0       0(A 제외 나머지 알파벳(K-1) or 1(A가 올 경우)
    1       0(A, B 제외 나머지 알파벳(K-2) or 1(A가 올 경우) or 2(B가 올 경우)
    2       0(A, C 제외 나머지 알파벳(K-2) or 3(C가 올 경우) or 5(A가 올 경우)
    3       0(A, B 제외 나머지 알파벳(K-2) or 1(A가 올 경우) or 4(B가 올 경우)
    4       0(A, C 제외 나머지 알파벳(K-2) or 1(A가 올 경우), C가 오면 안됨
    5       0(A, B 제외 나머지 알파벳(K-2) or 1(A가 올 경우) or 6(B가 올 경우)
    6       0(A, C 제외 머지 알파벳(K-2) or 5(A가 올 경우), C가 오면 안됨
'''
mod = 1000000009
dp = [[0] * 7 for _ in range((N+1))]

dp[0][0] = 1
for i in range(1, N+1):
    dp[i][0] = dp[i-1][0] * (K-1)
    for j in range(1, 7):
        dp[i][0] += dp[i-1][j] * (K-2)

    dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5]

    dp[i][2] = dp[i-1][1]
    dp[i][3] = dp[i-1][2]
    dp[i][4] = dp[i-1][3]
    dp[i][5] = dp[i-1][2] + dp[i-1][6]
    dp[i][6] = dp[i-1][5]
    for j in range(7):
        dp[i][j] %= mod

answer = 0
for j in range(7):
    answer += dp[N][j]
    answer %= mod

print(answer)