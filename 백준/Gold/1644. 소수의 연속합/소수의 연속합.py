import math
N = int(input())

# 에라토스테네스의 체로 소수 먼저 구하기
nums = [False, False] + [True] * (N-1)

prime_nums = []

if N == 1:
    print(0)
    exit()

for i in range(2, int(math.sqrt(N)+ 1)):
    if nums[i] == True:
        j = 2
        while i * j <= N:
            nums[i*j] = False
            j += 1
for i in range(2, N+1):
    if nums[i] == True:
        prime_nums.append(i)

# 소수 연속으로 더해서 N 되는 경우 구하기
start = 0
end = 0

total = prime_nums[0]
ans = 0

while start <= end:
    if total > N:
        total -= prime_nums[start]
        start += 1
    else:
        if total == N:
            ans += 1
        end += 1
        if end == len(prime_nums):
            break
        total += prime_nums[end]
print(ans)