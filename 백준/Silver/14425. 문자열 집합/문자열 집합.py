import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for _ in range(N):
    line = input().rstrip()
    S.add(line)
# print(S)

ans = 0
for _ in range(M):
    arr = input().rstrip()
    if arr in S:
        ans += 1
print(ans)