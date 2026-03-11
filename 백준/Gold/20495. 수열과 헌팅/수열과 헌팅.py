import sys
input = sys.stdin.readline
N = int(input())
minus = [0] * N
plus = [0] * N

for i in range(N):
    a, b = map(int, input().split())
    minus[i] = a - b
    plus[i] = a + b

sort_minus = sorted(minus)
sort_plus = sorted(plus)

# 이분탐색
for i in range(N):
    s = 0
    e = N-1

    # 최솟값 탐색
    while s <= e:
        mid = (s + e) // 2
        if sort_plus[mid] >= minus[i]:
            e = mid - 1
        else:
            s = mid + 1
    print(s+1, end=" ")

    # 최댓값 탐색
    s = 0
    e = N-1
    while s <= e:
        mid = (s + e) // 2
        if sort_minus[mid] <= plus[i]:
            s = mid + 1
        else:
            e = mid - 1
    print(e+1)