import sys
input = sys.stdin.readline

N = int(input())
trees = []
tmp = []
for i in range(N):
    tree = int(input())
    trees.append(tree)
    if i > 0:
        tmp.append(trees[i] - trees[i-1])

max_v = tmp[0]

# 각 나무들 사이의 거리의 최대 공약수 구하기
def gcd(a, b): # gcd : Greatest Common Divisor
    while b > 0:
        a, b = b, a % b
    return a

for i in range(1, len(tmp)):
    max_v = gcd(max_v, tmp[i])

ans = 0
for i in range(len(tmp)):
    ans += (tmp[i] // max_v) - 1

print(ans)