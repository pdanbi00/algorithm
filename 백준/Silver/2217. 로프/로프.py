import sys
input = sys.stdin.readline
N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()
ans = 0
for i in range(len(rope)):
    ans = max(ans, rope[i] * (len(rope) - i))
print(ans)