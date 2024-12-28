from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
eww = set()
for _ in range(M):
    a, b = map(int, input().split())
    for i in range(1, N+1):
        if i != a and i != b:
            arr = [a, b, i]
            arr.sort()
            arr = tuple(arr)
            eww.add(arr)
tmp = 0
answer = 0
for com in combinations(nums, 3):
    if com in eww:
        tmp += 1
    answer += 1

print(answer - tmp)