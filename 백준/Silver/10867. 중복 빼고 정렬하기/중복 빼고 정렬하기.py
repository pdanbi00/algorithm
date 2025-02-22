import sys
input = sys.stdin.readline

N = int(input())
nums = set(list(map(int, input().split())))
arr = []
for n in nums:
    arr.append(n)

arr.sort()
print(*arr)