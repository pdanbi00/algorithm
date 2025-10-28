import sys
input = sys.stdin.readline
N, D = map(int, input().split())
presents = []

for _ in range(N):
    P, V = map(int, input().split())
    presents.append((P, V))
presents.sort()
left = 0
right = 0
total = 0
ans = 0
while True:
    if presents[right][0] - presents[left][0] < D:
        total += presents[right][1]
        right += 1

    else:
        ans = max(ans, total)
        tmp = presents[right][0] - D + 1
        while tmp > presents[left][0]:
            total -= presents[left][1]
            left += 1

    if right == N:
        break

ans = max(ans, total)
print(ans)