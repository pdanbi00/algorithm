import sys
input = sys.stdin.readline
N = int(input())
expected = []
for _ in range(N):
    expected.append(int(input()))

expected.sort()

# 불만족 합
answer = 0
for i in range(1, N+1):
    answer += abs(i - expected[i-1])
print(answer)