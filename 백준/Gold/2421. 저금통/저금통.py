# 에라토스테네스의 체
sieve = [1 for _ in range(1000001)]
sieve[0] = 0
sieve[1] = 0
for i in range(2, 1001):
    if sieve[i]:
        for j in range(i * 2, 1000001, i):
            sieve[j] = 0

prime = set()
for i in range(12, 1000001):
    if sieve[i]:
        prime.add(i)

def isPrime(a, b):
    num = int(str(a) + str(b))
    if num in prime:
        return 1
    return 0

# dp[i][j] : 첫번째 저금통에 i원을 넣고 두번째 저금통에 j원을 넣었을 때 소수가 가장 많이 나온 횟수

N = int(input())
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + isPrime(i, j)

print(dp[N][N])