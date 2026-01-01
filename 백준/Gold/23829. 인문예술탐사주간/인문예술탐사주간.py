from copy import deepcopy
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
trees = sorted(list(map(int, input().split())))
trees_sum = deepcopy(trees)

for i in range(1, N):
    trees_sum[i] += trees_sum[i-1]

for _ in range(Q):
    X = int(input())

    s, e = 0, N-1

    if trees[-1] <= X:
        print((N * X) - trees_sum[-1])
    elif trees[0] >= X:
        print(trees_sum[-1] - (N * X))
    else:
        while s <= e:
            mid = (s + e) // 2
            if trees[mid] >= X:
                e = mid - 1
            else:
                s = mid + 1

        print(((X * s) - trees_sum[s-1]) + (trees_sum[-1] - trees_sum[s-1] - (X * (N-s))))