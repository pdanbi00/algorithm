N, K = map(int, input().split())
children = list(map(int, input().split()))
diff = []

for i in range(1, N):
    tmp = children[i] - children[i-1]
    diff.append(tmp)

diff.sort()

print(sum(diff[:N-K]))