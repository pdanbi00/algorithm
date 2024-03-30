import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
arr.sort(reverse=True)
for n in arr:
    print(n)